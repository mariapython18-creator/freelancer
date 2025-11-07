

# Create your views here.
from django.shortcuts import render,redirect
from .forms import Apply_form,Submit_form
from .models import  ApplyJob,Submit_job
from django.views import View
from .forms import Apply_form

class Apply_job(View):
    def get(self, request):
        if not request.user.is_authenticated or request.user.role != 'freelancer':
            return render(request, 'not_allowed.html')  # Show a simple “Not allowed” page

        form = Apply_form()
        return render(request, 'apply.html', {'form': form})

    def post(self, request):
        if not request.user.is_authenticated or request.user.role != 'freelancer':
            return render(request, 'not_allowed.html')

        form = Apply_form(request.POST, request.FILES)
        if form.is_valid():
            apply_job = form.save(commit=False)
            apply_job.applicant = request.user  # Automatically assign logged-in user
            apply_job.save()
            return render(request,'success.html')
        else:
            print(form.errors)
            return render(request, 'apply.html', {'form': form})


class Submit_jobapplication(View):
    def get(self, request):
        if not request.user.is_authenticated or request.user.role != 'freelancer':
            return render(request, 'not_allowed.html')  # show a “not allowed” page

        form = Submit_form()
        return render(request, 'submit.html', {'form': form})

    def post(self, request):
        if not request.user.is_authenticated or request.user.role != 'freelancer':
            return render(request, 'not_allowed.html')

        form = Submit_form(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.Applicant_name = request.user  # set the logged-in freelancer automatically
            submission.save()
            return render(request,'success.html')
        else:
            return render(request, 'submit.html', {'form': form})
from django.shortcuts import  get_object_or_404
from client.models import Job
class Job_Status(View):
    def get(self,request, id):
        job=Job.objects.get(id=id)
        application = ApplyJob.objects.filter(applicant=request.user, job=job).first()
        return render(request, 'job_status.html', {
            'job': job,
            'application':application})

from .models import Tutorial

class TutorialListView(View):
    def get(self, request):
        tutorials = Tutorial.objects.all().order_by('-created_at')
        return render(request, 'tutorial_list.html', {'tutorials': tutorials})
