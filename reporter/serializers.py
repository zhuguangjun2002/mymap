from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Fiberbox


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class FiberboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fiberbox
        fields = ('name','created_at','updated_at')


