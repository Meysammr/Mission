from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Driver,Mission
from . import serializers


class DriverListAPIView(APIView):

    def post(self, request):
        serializer = serializers.DriverSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
                return Response({'message': 'Driver is already assigned to a mission.'},status=status.HTTP_400_BAD_REQUEST)
            data['driver'] = driver.id
            serializer = serializers.MissionSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            driver.is_busy = True
            driver.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            serializer = serializers.MissionSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get(self, request):
        missions = Mission.objects.all()
        serializer = serializers.MissionSerializer(missions, many=True)
        return Response(serializer.data)
    


class MissionDetailAPIView(APIView):


    def patch(self, request, mission_id):
        try:
            mission = Mission.objects.get(id=mission_id)
            driver_id = request.data.get('driver')
            if driver_id is None:
                return Response({'message': 'Driver ID is required.'},status=status.HTTP_400_BAD_REQUEST)
            
            driver = Driver.objects.get(id=driver_id)
            if driver.is_busy:
                return Response({'message': 'Driver is already assigned to a mission.'},status=status.HTTP_400_BAD_REQUEST)
            
            mission.driver = driver
            mission.save()
            driver.is_busy = True
            driver.save()
            
            return Response({'message': 'Driver assigned successfully.'},status=status.HTTP_200_OK)
        except Mission.DoesNotExist:
            return Response({'message': 'Mission not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Driver.DoesNotExist:
            return Response({'message': 'Driver not found.'},status=status.HTTP_404_NOT_FOUND)