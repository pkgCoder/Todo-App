from .models import TODO
from django.contrib.auth.models import User
from tempus_dominus.widgets import  DateTimePicker
from django import forms

class TodoForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label="What to do")
    deadline = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        ),
    )
    class Meta:
        model = TODO
        fields = ['text', 'deadline', 'completed']