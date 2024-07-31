from django.contrib import admin
from .models import Appointment, Payment, Service, payment_service
# Register your models here.

admin.site.register(Appointment)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'service_cost',)

admin.site.register(Service,ServiceAdmin)
admin.site.register(Payment)

admin.site.register(payment_service)

