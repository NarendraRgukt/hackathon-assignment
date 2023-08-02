from django.urls import path
from account import views
app_name="account"

urlpatterns=[
    path("user/auth/token",views.UserTokenView.as_view(),name="user-token-generation-view"),
    path('user/create',views.UserCreate.as_view(),name="user-create"),
]