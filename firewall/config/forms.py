from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

from .models import FirewallRule


class FirewallRuleForm(forms.ModelForm):
    class Meta:
        model = FirewallRule
        fields = ['name', 'rule']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
