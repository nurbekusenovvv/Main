from django.urls import path
from .import views

urlpatterns = [
    path('car_form_submit/',views.car_form_submit, name='car_form_submit'),
]
