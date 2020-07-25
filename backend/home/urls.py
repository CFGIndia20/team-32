from django.urls import path
from . import views

urlpatterns = [
    path('Question/',views.questions, name = 'questions'),
    path('Feedback/',views.questions, name = 'questions'),
    path('dataEntry/',views.loadData, name = 'loadData'),
]
