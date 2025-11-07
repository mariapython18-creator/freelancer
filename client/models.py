from django.db  import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='categories')

    def __str__(self):
        return self.name

class Job(models.Model):
    job_name= models.CharField(max_length=100)
    description = models.TextField()
    vacancy=models.IntegerField()
    budget=models.IntegerField()
    Job_or_company_details = models.TextField(default="Not provided")
    Address = models.CharField(max_length=200, default="Not Provided")
    Location=models.CharField(max_length=200, default="Not Provided")
    Status = models.CharField(max_length=50, default='Not started yet')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_name





from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('freelancer', 'Freelancer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='freelancer')

    def __str__(self):
        return f"{self.username} ({self.role})"

from django.db import models
class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.FloatField()
    order_id = models.CharField(max_length=100, unique=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='payments_made',
        null=True,  # allow null temporarily
        blank=True
    )
    freelancer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='payments_received',
        null=True,
        blank=True
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

