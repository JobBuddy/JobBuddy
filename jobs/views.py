from django.shortcuts import render
from .models import Jobs


def home(request):
    context = {
        'jobs': Jobs.objects.all()
	}
    return render(request, 'jobs/home.html',context )


def company(request):
    return render(request, 'jobs/company.html')
