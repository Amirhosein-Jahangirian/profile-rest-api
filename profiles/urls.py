from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('profiles', views.ProfileViewSet, basename='profiles-general')

urlpatterns = [
    path('', include(router.urls)),
]
