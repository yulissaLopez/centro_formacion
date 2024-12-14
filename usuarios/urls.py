from django.urls import path
from .views import UserList
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path("", UserList.as_view(), name='usuarios_list'),
    # Authentication
    path('login/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
