from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.intro, name = "intro"),
    path('receive_sensor_data/', views.receive_sensor_data, name = "receive_sensor_data"),
    path("index/", views.index, name = "index"),
    path("sensor-data/", views.sensor_data, name = "sensor_data"),
    path("update_value/", views.update_value, name = "update_value"),
    path("water_value/", views.water_value, name="water_value"),
    path("temp/", views.temp, name = "temp"),
]