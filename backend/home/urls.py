from django.urls import path
from . import views

urlpatterns = [
    path('Questions/',views.questions, name = 'questions'),
]
