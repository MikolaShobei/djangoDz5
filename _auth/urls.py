from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshSlidingView

from _auth.views import RegisterView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='login'),
    path('/refresh', TokenRefreshSlidingView.as_view(), name='refresh_token'),
    path('/register', RegisterView.as_view())
]
