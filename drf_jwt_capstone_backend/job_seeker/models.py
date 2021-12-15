from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class SeekerProfile(models.Model):
    first_name = models.CharField(max_length =50, blank=True)
    last_name = models.CharField(max_length =50, blank=True)
    email= models.CharField(max_length =50, blank=True)
    phone_number = models.CharField(max_length =15, blank=True)
    user = models.ForeignKey('authentication.User', blank=True, null=True, on_delete=models.CASCADE)
    street = models.CharField(max_length =50, blank=True)
    city = models.CharField(max_length =50, blank=True)
    state = models.CharField(max_length =50, blank=True)
    zip_code = models.CharField(max_length =5, blank=True)
    jobs_applied_to = models.IntegerField(default=0)
    member_since = models.DateField( null=True, blank=True)


    def __str__(self):
        return self.first_name