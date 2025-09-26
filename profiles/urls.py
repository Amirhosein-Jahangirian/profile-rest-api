from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('profiles', views.ProfileViewSet, basename='profiles-general')

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
