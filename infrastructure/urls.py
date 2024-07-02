from django.urls import path
from .views import (
    BedListCreate, BedRetrieveUpdateDestroy,
    MedicineListCreate, MedicineRetrieveUpdateDestroy,
    EquipmentListCreate, EquipmentRetrieveUpdateDestroy
)

urlpatterns = [
    path('beds/', BedListCreate.as_view(), name='bed-list-create'),
    path('beds/<int:pk>/', BedRetrieveUpdateDestroy.as_view(), name='bed-detail'),
    path('medicines/', MedicineListCreate.as_view(), name='medicine-list-create'),
    path('medicines/<int:pk>/', MedicineRetrieveUpdateDestroy.as_view(), name='medicine-detail'),
    path('equipment/', EquipmentListCreate.as_view(), name='equipment-list-create'),
    path('equipment/<int:pk>/', EquipmentRetrieveUpdateDestroy.as_view(), name='equipment-detail'),
]

