from django.contrib import admin

from .models import ApplyJob, Submit_job, Tutorial

# Register your models here.
admin.site.register(ApplyJob)
admin.site.register(Submit_job)
admin.site.register(Tutorial)