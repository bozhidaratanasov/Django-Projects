from django import contrib
from django.conf.urls import include
from accounts.views import signout_user, signup_user, user_profile
from django.urls import path, include

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>/', user_profile, name='user profile'),
    path('profile/', user_profile, name='current user profile'),
    path('signup/', signup_user, name='signup user'),
    path('signout/', signout_user, name='signout user'),
]
