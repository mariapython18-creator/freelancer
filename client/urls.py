"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from client import views
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views


app_name='client'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Category_view.as_view(), name='category'),
    path('login', views.Login_view.as_view(), name='login'),
    path('register', views.Register_view.as_view(), name='register'),
    path('logout', views.Logout_view.as_view(), name='logout'),
    path('jobpost', views.Job_post.as_view(), name='jobpost'),
    path('Joblist', views.Job_list.as_view(), name='Job_list'),
    path('Jobdetails/<int:pk>/', views.Job_details.as_view(), name='Job_details'),
    path('applications/', views.ClientDashboard.as_view(), name='applications'),
    path('submissions/', views.Clientsubmissionview.as_view(), name='submissions'),
    path('accept/<int:id>/', views.Accept.as_view(), name='accept'),
    path('registration', views.Registration.as_view(), name='registration'),
    path('payment/',views.PaymentView.as_view(), name='payment'),
    path('payment/success/', views.PaymentSuccessView.as_view(), name='payment_success'),
    path('search', views.JobSearchView.as_view(), name='search'),



# Password Reset
path(
    'password-reset/',
    auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset.html',
        success_url=reverse_lazy('client:password_reset_done')  # <--- fix
    ),
    name='password_reset'
),
path(
    'password-reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
    name='password_reset_done'
),
path(
    'password-reset-confirm/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url=reverse_lazy('client:password_reset_complete')  # optional fix
    ),
    name='password_reset_confirm'
),
path(
    'password-reset-complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    name='password_reset_complete'
),
     path('job/edit/<int:pk>/', views.JobEditView.as_view(), name='edit_job'),
     path('job/delete/<int:pk>/', views.JobDeleteView.as_view(), name='delete_job'),
]



