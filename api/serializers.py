from django import forms
from rest_framework import serializers
class studentSerializer(serializers.Serializer):
    name =serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


