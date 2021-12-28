from rest_framework import serializers
from .models import Node
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class NodeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Node
        fields = (
            'id',
            'user',
            'content',
            'created_at',
        )
        read_only_fields = ('created_at',)