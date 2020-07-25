from django.urls import path
from . import views

urlpatterns = [
    path('Question/<str:phone_no>',views.questions, name = 'questions'),
    path('Feedback/',views.questions, name = 'questions'),
    path('dataEntry/',views.loadData, name = 'loadData'),
]
