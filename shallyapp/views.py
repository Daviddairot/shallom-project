from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SensorData, waterlevel  # Assuming you have a model to store sensor data
from django.core.serializers import serialize
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to home page after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'intro.html')



class CustomLoginView(LoginView):
    template_name = 'intro.html'
    redirect_authenticated_user = True



def logout_view(request):
    logout(request)
    return redirect('intro')



def index(request):
    username = request.user.username if request.user.is_authenticated else 'Guest'
    return render(request, 'index.html', {'username': username})


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


def statistics(request):
    return render(request, 'statistics.html')

def Information(request):
    return render(request, 'Information.html')



def get_latest_sensor_data(request):
    # Get the latest record
    try:
        latest_data = SensorData.objects.latest('created_at')
        data = {
            'value': latest_data.value,
            'water': latest_data.water,
            'temp': latest_data.temp,
            'created_at': latest_data.created_at,
        }
    except SensorData.DoesNotExist:
        data = {
            'value': None,
            'water': None,
            'temp': None,
            'created_at': None,
        }
    return JsonResponse(data)