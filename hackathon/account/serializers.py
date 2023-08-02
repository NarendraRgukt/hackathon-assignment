from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=('email','name','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'min_length':8
            }
        }

    def create(self,validated_data):
        '''validating the data while creating the user'''
        email=validated_data['email']
        password=validated_data['password']
        user=authenticate(request=self.context.get('request'),email=email,password=password)
        if not user:
            return get_user_model().objects.create_user(**validated_data)
        else:
            raise serializers.ValidationError("Email already exists")
        

        
class UserTokenSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=255)
    password=serializers.CharField(max_length=255,style={
        'input_type':'password'
    },
    trim_whitespace=False
    )