from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SensorData, waterlevel  # Assuming you have a model to store sensor data
from django.core.serializers import serialize



def intro(request):
    return render(request, 'intro.html')

def index(request):
    return render(request, 'index.html')


@csrf_exempt
def receive_sensor_data(request):
    if request.method == 'POST':
        sensor_value = request.POST.get('sensorValue')
        SensorData.objects.all().delete()
        # Save the new SensorData object
        SensorData.objects.create(value=sensor_value)
        return JsonResponse({'message': 'Sensor data received successfully'}, status=200)
    elif request.method == 'GET':
        sensor_value = request.GET.get('sensorValue')
        waterlevel = request.GET.get('water')
        temperture = request.GET.get('temp')
        SensorData.objects.all().delete()
        # Save the new SensorData object
        SensorData.objects.create(value=sensor_value, water = waterlevel, temp = temperture)
        return JsonResponse({'message': 'Sensor data received successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Unsupported HTTP method'}, status=405)

def sensor_data(request):
    # Fetch the latest sensor data from the database
    latest_sensor_data = SensorData.objects.latest('value')  # Assuming 'id' is the primary key
    # Return the latest sensor value
    return JsonResponse({'value': latest_sensor_data.value})


def water_value(request):
    if request.method == 'GET':
        # Get the sensor value from the request query parameters
        sensor_value = request.GET.get('sensorValue')
        # Delete all existing water level data
        waterlevel.objects.all().delete()
        # Create a new water level object with the received value
        waterlevel.objects.create(value=sensor_value)
        # Return a success message as JSON response
        return JsonResponse({'message': 'Water level data received and updated successfully'}, status=200)
    else:
        # Return an error message for unsupported HTTP methods
        return JsonResponse({'error': 'Unsupported HTTP method'}, status=405)
    


def update_value(request):
    # Get the latest waterlevel object from the database
    latest_waterlevel = SensorData.objects.latest('created_at')

    # Extract the value from the latest waterlevel object
    new_value = latest_waterlevel.water

    # Return the value as JSON response
    return JsonResponse({'new_value': new_value})


def temp(request):
    # Get the latest waterlevel object from the database
    latest_templevel = SensorData.objects.latest('temp')

    # Extract the value from the latest waterlevel object
    new_value = latest_templevel.temp

    # Return the value as JSON response
    return JsonResponse({'new_value': new_value})


