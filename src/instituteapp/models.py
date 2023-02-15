from django.db import models

class ServicesData(models.Model):
    Course_Num=models.IntegerField()
    Course_Name=models.CharField(max_length=50)
    Starting_time=models.TimeField(max_length=50)
    Starting_Date=models.DateField(max_length=50)
    Duration=models.CharField(max_length=50)
    Fee=models.FloatField()
    Trainer_Name=models.CharField(max_length=50)


class FeedbackData(models.Model):
    Name=models.CharField(max_length=50)
    Rating=models.IntegerField()
    Date=models.DateTimeField()
    Feedback=models.CharField(max_length=500)

class ContactData(models.Model):
    F_Name=models.CharField(max_length=50)
    L_Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Mobile=models.BigIntegerField()
    Location=models.CharField(max_length=50)
