from django.shortcuts import render
from django.http import JsonResponse
from .models import UserSubmission  # Assuming you're storing form data

def home(request):
    return render(request, 'myapp/index.html')

def api_data(request):
    data = list(UserSubmission.objects.values())
    return JsonResponse(data, safe=False)
