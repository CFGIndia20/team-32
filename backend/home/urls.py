from django.urls import path
from . import views

urlpatterns = [
    path('Question/',views.questions, name = 'questions'),
    path('Feedback/',views.questions, name = 'questions'),
    path('questionEntry/',views.loadQuestions, name = 'loadQuestions'),
    path('userEntry/',views.loadUser, name = 'loadUser'),
    path('feedbackEntry/',views.loadFeedback, name = 'loadFeedback'),
    path('dataEntry/',views.loadData, name = 'loadData'),
    path('feedbackEntry/',views.loadFeedback, name = 'loadFeedback'),
]
