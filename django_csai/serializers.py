from abc import ABC

from django.contrib.auth.models import User, Group
from rest_framework import serializers

from django_csai.models import UserProfile, Dictionary


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user


class DictionarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dictionary
        fields = ['word', 'label']




