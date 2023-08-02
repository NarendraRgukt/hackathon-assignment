from django.contrib import admin

from hackathonapp.models import Hackathon,Submission,Registration


class HackathonModel(admin.ModelAdmin):
    list_display=['title','submission_type','start_datetime','end_datetime']

class SubmissionModel(admin.ModelAdmin):
    list_display=["user","hackathon","name"]

class RegistrationModel(admin.ModelAdmin):
    list_display=["user","hackathon"]
admin.site.register(Hackathon,HackathonModel)
admin.site.register(Submission,SubmissionModel)
admin.site.register(Registration,RegistrationModel)
