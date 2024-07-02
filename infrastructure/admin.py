from django.contrib import admin

# Register your models here.
from .models import Bed, Medicine, Equipment

admin.site.register(Bed)
admin.site.register(Medicine)
admin.site.register(Equipment)

