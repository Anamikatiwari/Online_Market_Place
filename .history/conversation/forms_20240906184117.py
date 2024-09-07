from django import forms

from .models import ConversationMessage

class ConversationMessageform(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)