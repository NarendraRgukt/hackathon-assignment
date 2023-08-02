from django.urls import path
from hackathonapp import views


urlpatterns=[
    path('hackathon/create/',views.HackathonCreateAPI.as_view(),name="hackathon-create"),
    path('hackathon/list/',views.HackathonListAPI.as_view(),name="hackathon-list"),
    path('register/new/hackathon/',views.RegisterHackathonAPIView.as_view(),name="register-new-hackathon"),
    path('registered/hackathon/list/',views.RegisteredHackathonsListAPI.as_view(),name="registered-hackathon-list"),
    path('create/hackathon/submission/',views.SubmissionHackathonAPI.as_view(),name="hackathon-create-submission"),
    path('get/hackathon/submissions/',views.SubmissionListRetrieve.as_view(),name="submission-list-retrieve"),

]