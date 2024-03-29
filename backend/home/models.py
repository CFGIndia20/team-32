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

class Unit(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=30)

class Stay(models.Model):
    UserID = models.ForeignKey(User,on_delete = models.CASCADE)
    UnitID = models.ForeignKey(Unit, on_delete = models.CASCADE)
    members = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField()

class Donor(models.Model):
    id = models.IntegerField(primary_key=True)
    phone_no = models.CharField(max_length=15)

class Donate(models.Model):
    unit_no = models.ForeignKey(Unit, on_delete = models.CASCADE)
    donor_id = models.ForeignKey(Donor,on_delete = models.CASCADE)