from hackathonapp import models
from rest_framework import serializers

class HackathonSerializer(serializers.ModelSerializer):
    '''hackathon model serializer '''
    class Meta:
        model=models.Hackathon
        fields="__all__"


class SubmissionSerializer(serializers.ModelSerializer):
    '''submission model serializer'''
    class Meta:
        model=models.Submission
        exclude=("user",)  #excluding user field in the validation process

class RegisterSerializer(serializers.ModelSerializer):
    '''register model serializer'''
    class Meta:
        model=models.Registration
        fields=("hackathon",)   #including hackathon field only
        