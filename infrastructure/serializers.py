from rest_framework import serializers
from .models import Bed, Medicine, Equipment

class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = '__all__'

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'
