from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('profiles', views.ProfileViewSet, basename='profiles')
router.register('feeds', views.ProfileFeedViewSet, basename='profile-feed')

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
