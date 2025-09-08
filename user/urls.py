
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from user.views import CreateUserView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    #test
]