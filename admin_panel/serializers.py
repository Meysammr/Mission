from rest_framework import serializers

from django.contrib.auth import authenticate

from . import models


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            return data
        raise serializers.ValidationError('Invalid username or password')



class MissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Mission
        fields = '__all__'



class DriverSerializer(serializers.ModelSerializer):
    current_mission = MissionSerializer(read_only=True)
    past_missions = MissionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Driver
        fields = '__all__'



