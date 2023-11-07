# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Car
# from .serializers import CarSerializer

# # Create your views here.

# class CarViewSet(viewsets.ModelViewSet):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
    
# def car_form_submit(request):
#     if request.method == 'POST':
#         car_make = request.POST['car_make']

#         car = Car.objects.create(make=car_make)
#         serialiser = CarSerializer(data = request.POST)
#     if serialiser.is_valid():
#         car = serialiser.save()
        
from django.shortcuts import render
from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
@api_view(['POST'])
def car_form_submit(request):
    if request.method == 'POST':
        car_make = request.data.get('car_make')  # Изменено на request.data.get

        serializer = CarSerializer(data={'make': car_make})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    

