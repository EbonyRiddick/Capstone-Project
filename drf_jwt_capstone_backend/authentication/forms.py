from django import forms
from . models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    """This form allows our custom user model to be registered with an added field reflecting its employee status"""
    is_company = forms.BooleanField(label="Check to register as a company", required=False)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "is_company")

    def save(self, commit=True):
        # Overriding the save method to add user to auth group of Employee or Customer depending on if box is checked
        user = super(CustomUserForm, self).save(commit=False)
        user.is_company = self.cleaned_data["is_company"]

        # If you get an exception here, you need to create the Employee/Customer groups in the Admin interface
        if commit:
            user.save()
            if user.is_company:
                poster = Group.objects.get(name="Poster")
                poster.user_set.add(user)
            else:
                seeker = Group.objects.get(name="Seeker")
                seeker.user_set.add(user)
        return user


