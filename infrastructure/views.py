from rest_framework import generics
from .models import Bed, Medicine, Equipment
from .serializers import BedSerializer, MedicineSerializer, EquipmentSerializer
from .filters import BedFilter, MedicineFilter, EquipmentFilter
from django_filters.rest_framework import DjangoFilterBackend

# CRUD for Bed
class BedListCreate(generics.ListCreateAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BedFilter

class BedRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer


# CRUD for Medicine
class MedicineListCreate(generics.ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MedicineFilter
class MedicineRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


# CRUD for Equipment
class EquipmentListCreate(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EquipmentFilter

class EquipmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer