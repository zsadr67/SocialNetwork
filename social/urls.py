from django.urls import path

from social.views import ProfileView , PostView

urlpatterns = [
    path('profile/', ProfileView.as_view({'get': 'list' , 'post': 'create'  ,'delete': 'destroy' }), name='profile'),
    path('post/' , PostView.as_view({'get': 'list' , 'post': 'create' , 'put': 'update' ,'delete': 'destroy' })),
]