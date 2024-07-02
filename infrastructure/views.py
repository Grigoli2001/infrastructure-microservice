from django.shortcuts import render
from rest_framework import generics
from .models import Bed, Medicine, Equipment
from .serializers import BedSerializer, MedicineSerializer, EquipmentSerializer
# Create your views here.

# CRUD for Bed
class BedListCreate(generics.ListCreateAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

class BedRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

# CRUD for Medicine
class MedicineListCreate(generics.ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class MedicineRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

# CRUD for Equipment
class EquipmentListCreate(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class EquipmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer