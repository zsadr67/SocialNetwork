from django.urls import path

from social.views import ProfileView , PostView ,FollowView , FollowingListView , FollowerListView

urlpatterns = [
    path('profile/', ProfileView.as_view({'get': 'list' , 'post': 'create'  ,'delete': 'destroy' }), name='profile'),
    path('profile/<int:user_id>/', ProfileView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('post/' , PostView.as_view({'get': 'list' , 'post': 'create' , 'put': 'update' ,'delete': 'destroy' })),
    path('post/<int:pk>/', PostView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('post/<int:post_id>/like/', PostView.as_view({'post': 'like'})),
    path('follow/<int:user_id>/', FollowView.as_view()),
    path('following/<int:user_id>/', FollowingListView.as_view()),
    path('follower/<int:user_id>/', FollowerListView.as_view()),

]