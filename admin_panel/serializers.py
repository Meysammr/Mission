from rest_framework import serializers

from . import models


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Driver
        fields = '__all__'


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mission
        fields = '__all__'
