from django.urls import path, include
from rest_framework import routers

from django_csai.views import UserViewSet, GroupViewSet, DictionaryViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'dictionary', DictionaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
]