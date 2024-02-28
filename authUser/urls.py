from django.urls import path
from .views import RegisterUser, LoginView, ChangePasswordView, UpdateUserView
# from rest_framework_simplejwt import views as jwt_views
app_name = 'authUser'

urlpatterns = [
    path('register', RegisterUser.as_view()),
    path('login', LoginView.as_view()),
    path('change-password', ChangePasswordView.as_view()),
    path('update-user', UpdateUserView.as_view()),
]

