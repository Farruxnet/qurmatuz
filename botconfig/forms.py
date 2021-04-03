from django import forms
from django.utils import timezone
from . models import Messages

class MessagesForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    # date = forms.DateTimeField(default=timezone.now)
    class Meta:
        model = Messages
        fields = ['text']
