from django.contrib import admin
from django.urls import path

from user.views import CreateUserView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
]