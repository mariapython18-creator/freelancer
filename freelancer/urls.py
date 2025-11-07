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
from freelancer import views
from .views import TutorialListView

app_name='freelancer'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('apply', views.Apply_job.as_view(), name='apply'),
    path('submit', views.Submit_jobapplication.as_view(), name='submit'),
    path('jobs/<int:id>/', views.Job_Status.as_view(), name='job_status'),
    path('tutorials/', TutorialListView.as_view(), name='tutorial_list'),

]

