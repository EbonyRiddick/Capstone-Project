from rest_framework import serializers
from . models import Seeker

class SeekerSerializer(serializers.ModelSerializer):
        class Meta:
            model = Seeker
            # If added new columns through the User model, add them in the fields
            # list as seen below
            fields = ('first_name', 'last_name', 'email','username', 'street','city', 'state', 'zip_code', 'jobs_applied_to', 'member_since')