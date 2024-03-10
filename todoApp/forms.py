from .models import Task
from django import forms
from django.forms import ModelForm

class TaskForm(ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = Task
        fields = ('__all__')