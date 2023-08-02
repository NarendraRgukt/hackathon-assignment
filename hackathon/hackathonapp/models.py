from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()

class Hackathon(models.Model):
    # Fields
    title = models.CharField(max_length=200)
    description = models.TextField()
    background_image = models.ImageField(upload_to='hackathon_backgrounds/')    #uploading it to the media/hackathon-backgrounds/  directory
    hackathon_image = models.ImageField(upload_to='hackathon_images/')  #uploading it to the media/hackathon-images/  directory
    submission_type_choices = [         #predefining types
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    ]
    submission_type = models.CharField(max_length=10, choices=submission_type_choices)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
    


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)        #one to many relationship with user model
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)      #one to many relationship with hackathon model

    def __str__(self):
        return f"{self.user.email} - {self.hackathon.title}"
    

class Submission(models.Model):
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE, related_name='submissions')  #related_name-accessing submissions through hackathon model
    user = models.ForeignKey(User, on_delete=models.CASCADE)    #CASCADE-if user object deletes this object will also be deleted
    name = models.CharField(max_length=200)
    summary = models.TextField()
    submission_file = models.FileField(upload_to='submissions/file', blank=True, null=True)#depending upon the type of submission user can store the data of submission
    submission_link = models.URLField(blank=True,null=True)

    def __str__(self):
        return f"{self.name} - {self.hackathon.title}"

