"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from backend.api import views

router = routers.DefaultRouter()
router.register(r'library-games', views.LibraryGameViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'players', views.PlayerViewSet)
# router.register(r'owners', views.OwnerViewSet)
router.register(r'withdraw', views.WithdrawViewSet)

urlpatterns = [
    path('auth/', include('rest_framework.urls')),

    # http://localhost:8000/api/admin/
    path('admin/', admin.site.urls),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),


    # Authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
