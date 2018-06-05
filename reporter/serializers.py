from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import FiberBox


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class FiberBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiberBox
        fields = ('name','created_at','updated_at')


