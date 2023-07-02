from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=100)
    is_busy = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    
    

class Mission(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pickup_address = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=100)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

   