from django.db import models

class Question(models.Model):
    id = models.IntegerField(primary_key = True)
    question = models.CharField(max_length = 500)

class User(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    address = models.CharField(max_length = 500)
    phone_no = models.CharField(max_length = 15)
    language = models.CharField(max_length = 20)
    
class Feedback(models.Model):
    id = models.IntegerField(primary_key = True)
    question_id = models.ForeignKey(Question, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    response = models.IntegerField()
    unit_no = models.IntegerField()

