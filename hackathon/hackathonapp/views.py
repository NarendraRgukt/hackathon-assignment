from hackathonapp import serializers,models

from rest_framework.generics import CreateAPIView,GenericAPIView
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.core import validators

class HackathonCreateAPI(CreateAPIView):
    '''creating hackathon view'''
    serializer_class=serializers.HackathonSerializer
    queryset=models.Hackathon.objects.all()
    authentication_classes=[authentication.TokenAuthentication] #using token authentication
    permission_classes=[permissions.IsAdminUser]    #admin user only creates the hackathon
    

    

class HackathonListAPI(GenericAPIView):
    '''retrieving all the hackathon list'''
    serializer_class=serializers.HackathonSerializer
    permission_classes=[permissions.IsAuthenticated]    #only authenticated user gets hackathon list
    authentication_classes=[authentication.TokenAuthentication] #for authentication wer use token authentication

    def get_queryset(self):
        return models.Hackathon.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)#converting complex queyset into python objects using serializer
        return Response(serializer.data, status=status.HTTP_200_OK)




class SubmissionHackathonAPI(CreateAPIView):
    '''creating a new submission'''
    serializer_class = serializers.SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated,]
    authentication_classes = [authentication.TokenAuthentication,]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.request.user
        hackathon = serializer.validated_data['hackathon']

        # Check if the user has already submitted to this hackathon
        if models.Submission.objects.filter(hackathon=hackathon, user=user).exists():
            return Response({'error': 'You have already submitted to this hackathon.'}, status=status.HTTP_400_BAD_REQUEST)

        # Determine the submission type based on the provided fields
        submission_type = None
        #checking for when the user submits both fields i.e submission_file and submission_link
        if serializer.validated_data.get('submission_file') is not None and serializer.validated_data.get('submission_link') is not None:
            return Response({'error': f'You are uploading both formats. This hackathon allows only {hackathon.submission_type} formats.'}, status=status.HTTP_400_BAD_REQUEST)
        elif 'submission_file' in serializer.validated_data:
            submission_type = 'file'
        elif 'submission_link' in serializer.validated_data:
            submission_type = 'link'

        # Validate submission type based on hackathon's allowed types
        if submission_type:
            if submission_type == 'file' and hackathon.submission_type != 'file':
                return Response({'error': 'This hackathon only allows url submissions.'}, status=status.HTTP_400_BAD_REQUEST)
            elif submission_type == 'link' and hackathon.submission_type != 'link':
                return Response({'error': 'This hackathon only allows file submissions.'}, status=status.HTTP_400_BAD_REQUEST)
        

        # Create a new submission
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class SubmissionListRetrieve(GenericAPIView):
    '''retrieving all the submissions done by the user '''
    serializer_class=serializers.SubmissionSerializer
    permission_classes=[permissions.IsAuthenticated] #user needs to be authenticated
    authentication_classes=[authentication.TokenAuthentication] 
    
    def get_queryset(self):
        return models.Submission.objects.filter(user=self.request.user) #returning all the submission objects related to the user
    
    def get(self,request,*args,**kwargs):
        serializer=self.serializer_class(self.get_queryset(),many=True)#allowing many objects from model
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class RegisterHackathonAPIView(CreateAPIView):
    '''registering for the new hackathon api '''
    serializer_class=serializers.RegisterSerializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]
    def post(self,request,*args,**kwargs):
        '''overriding the create function'''
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        registerquery=models.Registration.objects.filter(hackathon=serializer.validated_data['hackathon'],user=request.user)
        if registerquery.exists():#checking wheter the user registered to the hackathon or not
            return Response({'error':'already registered to this hackathon'},status=status.HTTP_400_BAD_REQUEST)
        else:   # if not registered register to the new hackathon
            self.perform_create(serializer)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    def perform_create(self,serializer):
        return serializer.save(user=self.request.user)

class RegisteredHackathonsListAPI(GenericAPIView):
    '''retrieving all the registered hackathon lists'''
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]
    serializer_class=serializers.RegisterSerializer
    
    def get_queryset(self):
        return models.Registration.objects.filter(user=self.request.user)
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        
        hackathon_ids = [item['hackathon'] for item in serializer.data]#all the hackatho id's the user registered
        hackathon_items = models.Hackathon.objects.filter(id__in=hackathon_ids)#returning hackathon items which the user registers
        # Serialize the Hackathon objects into JSON
        serializer_hackathon=serializers.HackathonSerializer(hackathon_items,many=True)

        return Response(serializer_hackathon.data, status=status.HTTP_200_OK)

    
    






