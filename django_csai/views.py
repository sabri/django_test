from django.contrib.auth.models import Group

from rest_framework import viewsets

from rest_framework import permissions

from django_csai.models import User, Dictionary
from django_csai.serializers import UserSerializer, GroupSerializer, DictionarySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class DictionaryViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = [permissions.IsAuthenticated]
