from django import forms
from .models import User


class NewUserForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label="First Name", widget=forms.TextInput(
        attrs={"class": "form-control"}))
    last_name = forms.CharField(required=True, label="Last Name", widget=forms.TextInput(
        attrs={"class": "form-control"}))
    mobile = forms.CharField(label="Mobile", widget=forms.NumberInput(
        attrs={"class": "form-control"}))
    email = forms.EmailField(required=True, label="Email", widget=forms.EmailInput(
        attrs={"class": "form-control"}))
    password = forms.CharField(required=True, label="Password", widget=forms.PasswordInput(
        attrs={"class": "form-control"}))

    # validation
    def clean_first_name(self):
        first = self.cleaned_data['first_name']
        if len(first) < 3:
            raise forms.ValidationError('minimum 3 characters')
        return first

    def clean_last_name(self):
        second = self.cleaned_data['last_name']
        if len(second) < 3:
            raise forms.ValidationError('minimum 3 characters')
        return second

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise forms.ValidationError('minimum 6 characters')
        return password

    class Meta:
        model = User
        fields = ("first_name", "last_name", "mobile",
                  "email", "password")
