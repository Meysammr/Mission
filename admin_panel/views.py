from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Driver,Mission
from . import serializers


class DriverListAPIView(APIView):

    def post(self, request):
        serializer = serializers.DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        drivers = Driver.objects.all()
        serializer = serializers.DriverSerializer(drivers, many=True)
        return Response(serializer.data)
    

    
class MissionListAPIView(APIView):
    
    def post(self, request):
        data = request.data.copy()
        driver_id = data.get('driver')
        if driver_id:
            driver = Driver.objects.get(id=driver_id)
            if driver.is_busy:
                return Response({'message': 'Driver is already assigned to a mission.'},
                                 status=status.HTTP_400_BAD_REQUEST)
            data['driver'] = driver.id
            serializer = serializers.MissionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                driver.is_busy = True
                driver.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = serializers.MissionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        missions = Mission.objects.all()
        serializer = serializers.MissionSerializer(missions, many=True)
        return Response(serializer.data)
    

    
