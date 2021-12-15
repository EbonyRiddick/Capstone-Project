from django.db import models

# Create your models here.
class JobListings(models.Model):
    job_title = models.CharField(max_length =100, blank=True)
    user = models.ForeignKey('authentication.User', blank=True, null=True, on_delete=models.CASCADE)
    # user = models.ForeignKey('job_poster.company_name', max_length =50, blank=True, on_delete=models.CASCADE)
    zip_code = models.IntegerField ()
    description = models.CharField(max_length =500, blank=True)
    wage = models.IntegerField()
    start_date = models.DateField( null=True, blank=True)
    end_date = models.DateField( null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.job_title