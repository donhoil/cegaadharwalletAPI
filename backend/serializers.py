from rest_framework import serializers
from .models import Payment

class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields=['eid','status']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'
