from django import forms

from users.models import UserPro


class RegistForm(forms.Form):
    password = forms.CharField(required=True, min_length=5)

    # class Meta:
    #     model = UserPro
    #     fields = '__all__'