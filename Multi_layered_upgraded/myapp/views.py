from django.shortcuts import render
from django.http import JsonResponse
from .models import UserSubmission
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return render(request, 'myapp/index.html')

def api_data(request):
    data = list(UserSubmission.objects.values())
    return JsonResponse(data, safe=False)

@csrf_exempt
def submit_vote(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        vote = data.get('vote_option')  # 'vote_option' should match the frontend
        UserSubmission.objects.create(choice=vote)
        return JsonResponse({'status': 'success'})
