from django import forms
from .models import ToDo
class TaskForm(forms.ModelForm):
    """Form definition for Task."""

    class Meta:
        """Meta definition for Taskform."""

        model = ToDo
        fields = ('task',)
