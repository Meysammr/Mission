from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    driver_id = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def current_mission(self):
        return Mission.objects.filter(assigned_driver=self).first()

    def past_missions(self):
        return Mission.objects.filter(assigned_driver=self, is_completed=True)
    


class Mission(models.Model):
    assigned_driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    mission_id = models.AutoField(primary_key=True)
    source_address = models.CharField(max_length=200)
    destination_address = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return f'Mission {self.mission_id}'
