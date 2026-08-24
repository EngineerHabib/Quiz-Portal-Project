from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    USER_TYPE = [
        ('Admin','Admin'),
        ('Participant','Participant'),
    ]

    user_type = models.CharField(choices=USER_TYPE, max_length=30, null=True)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,null=True)
    institute = models.CharField(max_length=30,null=True)
    address = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.name

class QuizModel(models.Model):
    title = models.CharField(max_length=30,null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title

class QuestionModel(models.Model):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.text

class OptionModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, related_name='options')

    text = models.CharField(max_length=30,null=True)
    is_correct = models.BooleanField(null=True , default=0)

    def __str__(self):
        return self.text

class ExamModel(models.Model):
    participant = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    quiz = models.ForeignKey(QuizModel, on_delete=models.SET_NULL, null=True)
    score = models.IntegerField(null=True)

    
