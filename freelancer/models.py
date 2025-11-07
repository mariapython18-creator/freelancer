from django.db import models
from client.models import Job
from client.models import CustomUser
from django.conf import settings
# Create your models here.

class ApplyJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    Address=models.CharField(max_length=50)
    place=models.CharField(max_length=15)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    applied_on = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    contact_No=models.IntegerField()
    status = models.CharField(max_length=50, default='Pending')

class Submit_job(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='submissions')
    Address = models.CharField(max_length=50)
    place = models.CharField(max_length=15)
    Applicant_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project= models.FileField(upload_to='projects/')
    Submitted_on = models.DateTimeField(auto_now_add=True)
    Email = models.EmailField(unique=True, blank=False, null=False)
    Contact_No = models.IntegerField()
    Status = models.CharField(max_length=50, default='completed')
from django.db import models
from django.utils import timezone

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # For uploaded videos
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    # For embedded videos like YouTube
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
