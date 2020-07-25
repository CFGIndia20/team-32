from django.shortcuts import render
from django.http import JsonResponse
from .models import Question,Feedback,User
import json
import pandas as pd
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def questions(request):
    jsonResponse = {}
    questionList = []
    questions = Question.objects.all()
    for question in questions:
        json = {
            'Id':question.id,
            'Question':question.question
        }
        questionList.append(json)
    
    jsonResponse['Questions'] = questionList
    return JsonResponse(jsonResponse)
    