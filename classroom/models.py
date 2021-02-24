from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
import datetime

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Quiz(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(default = datetime.datetime(2021,2,28,10,00,00))
    end_date = models.DateTimeField(default = datetime.datetime(2021,2,28,12,00,00))
    is_published = models.BooleanField('I Want to Publish',default=False)
    duration = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')

    def __str__(self):
        return self.user.username



class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)
    optionA = models.CharField('OptionA', max_length=255, default = "A şıkkı")
    optionB = models.CharField('OptionB', max_length=255, default = "B şıkkı")
    optionC = models.CharField('OptionC', max_length=255, default = "C şıkkı")
    optionD = models.CharField('OptionD', max_length=255, default = "D şıkkı")
    optionE = models.CharField('OptionE', max_length=255, default=None, blank=True, null=True)
    def __str__(self):
        return self.text



class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
    date = models.DateTimeField(auto_now_add=True)

