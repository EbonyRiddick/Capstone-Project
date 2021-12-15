from .models import JobListings
from rest_framework import serializers


class JobListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListings
        fields = [ 'job_title', 'company', 'wage']
            


class JobListingsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListings
        fields = '__all__'