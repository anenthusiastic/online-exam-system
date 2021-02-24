from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from classroom.models import (Question)

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text','optionA','optionB','optionC','optionD','optionE')

