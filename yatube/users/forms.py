from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Contact
from django import forms

User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'body')

    def clean_subject(self):
        data = self.cleaned_data['subject']
        if 'thanks' not in data.lower().strip():
            raise forms.ValidationError('Поблагодарите меня')
        return data
