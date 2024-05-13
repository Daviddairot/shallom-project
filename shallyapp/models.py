from django.db import models

class SensorData(models.Model):
    value = models.CharField(max_length=100, null=True)  # Assuming the sensor value is a string
    water = models.CharField(max_length=100, null=True)
    temp = models.CharField(max_length=100, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sensor Data: {self.value} (created at {self.created_at})"

class waterlevel(models.Model):
    value = models.CharField(max_length=100, null=True)  # Assuming the sensor value is a string

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sensor Data: {self.value} (created at {self.created_at})"