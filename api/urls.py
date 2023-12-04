from django.urls import path , include
from rest_framework.routers import DefaultRouter
from userAuth.views import RegisterAPI , LoginAPI , LogoutAPI
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/', RegisterAPI.as_view() ),
    path('login/', LoginAPI.as_view() ),
    path('refresh_access_token/', TokenRefreshView.as_view()),
    path('logout/',LogoutAPI.as_view())
]
