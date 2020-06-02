from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def shreyas(request):
	jobs = Job.objects
	projects = Projects.objects
	skills = Skills.objects
	education = Education.objects
		
	return render(request, 'jobs/home.html', {'jobs': jobs , 'projects' : projects, 'skills': skills, 'education': education})
	
def detail(request, job_id):
	job_detail = get_object_or_404(Job, pk=job_id)
	return render(request, 'jobs/job_details.html', {'job' : job_detail})
