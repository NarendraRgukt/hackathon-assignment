from django.urls import path
from hackathonapp import views


urlpatterns=[
    path('hackathon/create',views.HackathonCreateAPI.as_view(),name="hackathon-create"),
    path('hackathon/get/all',views.HackathonListAPI.as_view(),name="hackathon-list"),
    path('register-hackathon/create',views.RegisterHackathonAPIView.as_view(),name="register-new-hackathon"),
    path('register-hackathon/get/all',views.RegisteredHackathonsListAPI.as_view(),name="registered-hackathon-list"),
    path('hackathon-submission/create',views.SubmissionHackathonAPI.as_view(),name="hackathon-create-submission"),
    path('hackathon-submission/get/all',views.SubmissionListRetrieve.as_view(),name="submission-list-retrieve"),

]