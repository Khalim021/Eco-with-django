from django import forms

from users.models import ProfileModel


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['user']
