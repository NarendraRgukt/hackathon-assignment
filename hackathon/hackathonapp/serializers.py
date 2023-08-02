from hackathonapp import models
from rest_framework import serializers

class HackathonSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Hackathon
        fields="__all__"


class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Submission
        exclude=("user",)  

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Registration
        fields=("hackathon",)
        