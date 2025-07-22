
from django.contrib import admin
from .models import Patient, Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization']
    search_fields = ['name', 'specialization']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'assigned_doctor', 'appointment_date']
    list_filter = ['assigned_doctor', 'appointment_date', 'gender']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    date_hierarchy = 'appointment_date'
# Register your models here.
