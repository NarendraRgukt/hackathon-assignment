from hackathonapp import serializers,models

from rest_framework.generics import CreateAPIView,GenericAPIView
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework import status


class HackathonCreateAPI(CreateAPIView):
    serializer_class=serializers.HackathonSerializer
    queryset=models.Hackathon.objects.all()
    authentication_classes=[authentication.TokenAuthentication,]
    permission_classes=[permissions.IsAdminUser,]
    

    

class HackathonListAPI(GenericAPIView):
    serializer_class=serializers.HackathonSerializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]
    queryset=models.Hackathon.objects.all()

    def get_queryset(self):
        return models.Hackathon.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class SubmissionHackathonAPI(CreateAPIView):
    serializer_class=serializers.SubmissionSerializer
    permission_classes=[permissions.IsAuthenticated,]
    authentication_classes=[authentication.TokenAuthentication]

    def perform_create(self,serializer):
        return serializer.save(user=self.request.user)
    

class RegisterHackathonAPIView(CreateAPIView):
    serializer_class=serializers.RegisterSerializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]
    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        registerquery=models.Registration.objects.filter(hackathon=serializer.validated_data['hackathon'],user=request.user)
        if registerquery.exists():
            return Response({'error':'already registered to this hackathon'},status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_create(serializer)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    def perform_create(self,serializer):
        return serializer.save(user=self.request.user)

class RegisteredHackathonsListAPI(GenericAPIView):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]
    serializer_class=serializers.RegisterSerializer
    
    def get_queryset(self):
        return models.Registration.objects.filter(user=self.request.user)
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        
        hackathon_ids = [item['hackathon'] for item in serializer.data]
        hackathon_items = models.Hackathon.objects.filter(id__in=hackathon_ids)
        # Serialize the Hackathon objects into JSON
        serializer_hackathon=serializers.HackathonSerializer(hackathon_items,many=True)

        return Response(serializer_hackathon.data, status=status.HTTP_200_OK)

    
    




class SubmissionListRetrieve(GenericAPIView):
    serializer_class=serializers.SubmissionSerializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]
    
    def get_queryset(self):
        return models.Submission.objects.filter(user=self.request.user)
    
    def get(self,request,*args,**kwargs):
        serializer=self.serializer_class(self.get_queryset(),many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

