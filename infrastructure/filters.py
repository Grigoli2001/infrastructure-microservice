import django_filters
from .models import Bed, Medicine, Equipment

class BedFilter(django_filters.FilterSet):
    class Meta:
        model = Bed
        fields = {
            'name': ['exact', 'icontains'],
            'type': ['exact'],
            'status': ['exact'],
        }

class MedicineFilter(django_filters.FilterSet):
    class Meta:
        model = Medicine
        fields = {
            'name': ['exact', 'icontains'],
            'category': ['exact'],
            'expiry_date': ['exact', 'gt', 'lt'],
        }

class EquipmentFilter(django_filters.FilterSet):
    class Meta:
        model = Equipment
        fields = {
            'name': ['exact', 'icontains'],
            'category': ['exact'],
            'status': ['exact'],
        }
