from django.forms import ModelForm
from .models import *

class TitleForm(ModelForm):
    class Meta:
        model = Board
        fields = ['title']

class ContextForm(ModelForm):
    class Meta:
        model = Board
        fields = ['context']

class DateForm(ModelForm):
    class Meta:
        model = Board
        fields = ['date']

