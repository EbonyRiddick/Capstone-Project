from rest_framework import serializers
from . models import SeekerProfile

class SeekerSerializer(serializers.ModelSerializer):
        class Meta:
            model = SeekerProfile
            # If added new columns through the User model, add them in the fields
            # list as seen below
            fields = ('id','first_name', 'last_name', 'user', 'street','city', 'state', 'zip_code', 'jobs_applied_to', 'member_since')