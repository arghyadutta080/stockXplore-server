from django.urls import path

from .views import HelloWorldView
from .auth import LoginAPIView, SignupAPIView, LogoutAPIView, IsAuthenticatedAPIView

urlpatterns = [
    path('', HelloWorldView.as_view(), name='hello_world'),
    path('auth/login/', LoginAPIView.as_view(), name='login'),
    path('auth/signup/', SignupAPIView.as_view(), name='signup'),
    path('auth/logout/', LogoutAPIView.as_view(), name='logout'),
    path('auth/isauth/', IsAuthenticatedAPIView.as_view(), name='is_authenticated'),
]
