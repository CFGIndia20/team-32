from django.shortcuts import render
from django.http import JsonResponse
from .models import Question,Feedback,User
import json
from .databaseEntry import addQuestions
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

@csrf_exempt 
def feedback(request):
    

@csrf_exempt    
def loadQuestions(request):
    if request.method != "POST":
        return JsonResponse({"data":"use post"})

    questions = addQuestions()
    for question in questions:
        temp = Question(id = question["id"],question = question["Question"])
        temp.save()

    return JsonResponse({"success":"True"})

@csrf_exempt    
def loadFeedback(request):
    if request.method != "POST":
        return JsonResponse({"data":"use post"})

    feedbacks = addFeedbacks()
    for feedback in feedbacks:
        temp = Feedback(id = question["id"],question = question["Question"])
        temp.save()

    return JsonResponse({"success":"True"})