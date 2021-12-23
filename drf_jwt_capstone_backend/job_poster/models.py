from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class PosterProfile(models.Model):
    company_name = models.CharField(max_length =50, blank=True)
    email= models.CharField(max_length =50, blank=True)
    phone_number = models.CharField(max_length =15, blank=True)
    user = models.ForeignKey('authentication.User', blank=True, null=True, on_delete=models.CASCADE)
    street = models.CharField(max_length =50, blank=True)
    city = models.CharField(max_length =50, blank=True)
    state = models.CharField(max_length =50, blank=True)
    zip_code = models.CharField(max_length =50, blank=True)
    jobs_posted = models.CharField(max_length =50, blank=True, default = 0)
    is_company = models.BooleanField(default = True)
   


    def __str__(self):
        return self.company_name