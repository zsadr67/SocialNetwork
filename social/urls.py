from django.urls import path

from social.views import ProfileView

urlpatterns = [
    path('profile/', ProfileView.as_view({'get': 'list' , 'post': 'create'  ,'delete': 'destroy' }), name='profile'),
]