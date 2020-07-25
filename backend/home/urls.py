from django.urls import path
from . import views

urlpatterns = [
    path('Questions/',views.questions, name = 'questions'),
    path('Feedback/',views.questions, name = 'questions'),
    path('questionEntry/',views.loadQuestions, name = 'loadQuestions'),
]
