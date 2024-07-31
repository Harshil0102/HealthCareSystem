from django.db import models
from accounts.models import User
# Create your models here.

STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('cancelled', 'Cancelled'),
    )


class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointments')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
    date = models.DateField()
    time = models.CharField(max_length=100)
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f'Appointment of {self.patient.first_name} with DR.{self.doctor.first_name} on {self.date}'
    

class Service(models.Model):
    service_name = models.CharField(max_length=255)
    service_cost = models.DecimalField(max_digits=8, decimal_places=2)

PAYMENT_CHOICES = (
      ('CASH','CASH'),
      ('CHECK','CHECK'),
      ('CARD','CARD'),
)

class Payment(models.Model):
    appointment = models.ForeignKey(Appointment, null=True, blank=True , on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True , on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='CASH')
    created_at = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)

class payment_service(models.Model):
     payment = models.ForeignKey(Payment, null=True, blank=True,on_delete=models.CASCADE)
     service = models.ForeignKey(Service, null=True, blank=True,on_delete=models.CASCADE)

    #  def __str__(self):
    #       return self.payment.user.username,self.service.service_name
