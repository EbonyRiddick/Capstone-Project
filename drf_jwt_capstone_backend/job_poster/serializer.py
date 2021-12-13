from rest_framework import serializers
from . models import PosterProfile

class PosterSerializer(serializers.ModelSerializer):
        class Meta:
            model = PosterProfile
            # If added new columns through the User model, add them in the fields
            # list as seen below
            fields = ('id','company_name',  'user', 'phone_number', 'email', 'street','city', 'state', 'zip_code', 'jobs_posted')