from django.db.models.signals import post_save
from django.dispatch import receiver
from client. models import Job
from .models import ApplyJob,Submit_job

# When a freelancer applies
@receiver(post_save, sender=ApplyJob)
def update_job_status_on_apply(sender, instance, created, **kwargs):
    if created:  # Only for new applications
        job = instance.job
        job.status = "Pending"  # Or "In Progress" if you want
        job.save()

# When a freelancer submits work
@receiver(post_save, sender=Submit_job)
def update_job_status_on_submit(sender, instance, created, **kwargs):
    if created:  # Only for new submissions
        job = instance.job
        job.status = "Submitted"
        job.save()
