from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import FiberBoxes


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class FiberBoxesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiberBoxes
        fields = ('name','created_at','updated_at')

