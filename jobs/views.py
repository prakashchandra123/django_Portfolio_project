from django.shortcuts import render
from .models import job

# Create your views here.
def prakash(request):
    jobs=job.objects
    return render(request,'jobs/home.html',{'jobs':jobs})
def detail(request,job_id):
    print(job_id)
    return render(request,'jobs/home.html')
