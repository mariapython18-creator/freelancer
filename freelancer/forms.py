from  django import forms
from .models import ApplyJob,Submit_job
from django import forms
from .models import ApplyJob

class Apply_form(forms.ModelForm):
    class Meta:
        model = ApplyJob
        fields = ['job', 'Address', 'place', 'resume', 'email', 'contact_No']  # Remove 'applicant' from fields

from django import forms
from .models import Submit_job

class Submit_form(forms.ModelForm):
    class Meta:
        model = Submit_job
        fields = ['job', 'Address', 'place', 'project', 'Email', 'Contact_No']  # removed Applicant_name
