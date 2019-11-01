from django.shortcuts import render
from django.http import HttpResponse
from Sampleapp .models import Employee


# Create your views here.
def Employeeview(request):
    return render(request,template_name="index.html")
