from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect
from .forms import Register_Form,Job_form,Login_form

from .models import Job,Category,CustomUser
from django.views import View

from freelancer.models import Submit_job,ApplyJob

class Category_view(View):
    def get(self,request):
        c=Category.objects.all()
        context={'category':c}
        return render(request,'category.html',context)
class Job_post(View):
    def get(self, request):
        form = Job_form()
        return render(request, 'job.html', {'form': form})
    def post(self, request):
        form = Job_form(request.POST)
        if form.is_valid():
            job = form.save(commit=False)  # don’t save yet
            job.client = request.user      # automatically assign logged-in user
            job.save()
            return redirect('client:Job_list')
        return render(request, 'job.html', {'form': form})

class Job_list(View):
    def get(self,request):
        j=Job.objects.all()
        context={'list':j}
        return render(request,'job_list.html',context)

class Job_details(View):
    def get(self,request,pk):
        j=Job.objects.get(id=pk)
        context={'list':j}
        return render(request,'job_details.html',context)

class Registration(View):
    def get(self,request):
        form=Register_form()
        context={'form':form}
        return render(request,'register.html',context)
    def post(self,request):
        form=Register_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,"register.html")



from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from .forms import Login_form

class Login_view(View):
    def get(self, request):
        form = Login_form()
        context = {'form': form}
        return render(request, 'registration/login.html', context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {user.username}!")
            return redirect('client:category')  # main page
        else:
            messages.error(request, "Invalid username or password")
            form = Login_form()
            return render(request, 'registration/login.html', {'form': form})



class Logout_view(View):
    def get(self, request):
        logout(request)
        return redirect('client:login')
class ClientDashboard(View):
    def get(self, request):

        if not request.user.is_authenticated:
            return redirect('client:login')
                # Fetch all jobs posted by this client
        jobs = Job.objects.filter(client=request.user)

        # Build a dictionary: key = Job object, value = QuerySet of applications
        job_applications = {}
        for job in jobs:
            applications = ApplyJob.objects.filter(job=job)
            if applications.exists():  # Only add if there are applications
                job_applications[job] = applications

        return render(request, 'dashboard.html', {
            'jobs': jobs,
            'job_applications': job_applications,
        })
class Clientsubmissionview(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('client:login')

        # Fetch all jobs posted by this client
        jobs = Job.objects.filter(client=request.user).prefetch_related('submissions')

        return render(request, 'dashboardsubmission.html', {'jobs': jobs})

class Register_view(View):
    def get(self,request):
        form=Register_Form()
        context={'form':form}
        return render(request,'register.html',context)
    def post(self,request):
        form=Register_Form(request.POST)
        if form.is_valid():
            form.save()

            return redirect("client:login")
        else:
            return render(request, "register.html", {"form": form})

class Accept(View):
    def get(self,request,id):
        apply=ApplyJob.objects.get(id=id)
        context={'apply':apply}
        return render(request,'accept.html',context)
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.conf import settings
import razorpay
from .models import  Payment

# Razorpay client
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

class PaymentView(View):
    def get(self, request):
        submission_id = request.GET.get('submission_id')
        submission = get_object_or_404(Submit_job, id=submission_id)

        return render(request, 'payment_form.html', {
            'submission': submission,
            'job': submission.job
        })

    def post(self, request):
        submission_id = request.POST.get('submission_id')
        submission = get_object_or_404(Submit_job, id=submission_id)

        job = submission.job
        freelancer = submission.Applicant_name
        amount = job.budget * 100  # convert to paise

        # Razorpay order
        order = razorpay_client.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': 1
        })

        # Save Payment details
        Payment.objects.create(
            user=request.user,  # required field
            client=request.user,  # optional if you want to keep client field
            freelancer=freelancer,
            job=job,
            amount=job.budget,
            order_id=order['id']
        )

        return render(request, 'payment_form.html', {
            'submission': submission,
            'job': job,
            'order_id': order['id'],
            'razorpay_key': settings.RAZORPAY_KEY_ID,
            'amount': job.budget
        })

# Payment success page
class PaymentSuccessView(View):
    def get(self, request):
        messages.success(request, "Payment completed successfully!")
        return render(request, 'payment_success.html')

class Logout_iew(View):
    def get(self, request):
        logout(request)  # This clears the current user's session
        return redirect('/login/')

 # assuming your Job model already exists
from django.db.models import Q

class JobSearchView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        results = Job.objects.filter(
            Q(job_name__icontains=query) | Q(description__icontains=query)
        ) if query else []
        return render(request, 'search.html', {'results': results, 'query': query})

class JobEditView(View):

    def get(self, request, pk):
        job = get_object_or_404(Job, pk=pk, client=request.user)
        form = Job_form(instance=job)
        return render(request, 'jobedit.html', {'form': form, 'job': job})

    def post(self, request, pk):
        job = get_object_or_404(Job, pk=pk, client=request.user)
        form = Job_form(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('client:Job_list')
        return render(request, 'jobedit.html', {'form': form, 'job': job})
class JobDeleteView(View):

    def get(self, request, pk):
        job = get_object_or_404(Job, pk=pk, client=request.user)
        return render(request, 'job_delete.html', {'job': job})

    def post(self, request, pk):
        job = get_object_or_404(Job, pk=pk, client=request.user)
        job.delete()
        return redirect('client:Job_list')

