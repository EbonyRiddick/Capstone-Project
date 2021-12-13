from django.db import models

# Create your models here.
class JobListings(models.Model):
    job_title = models.CharField(max_length =50, blank=True)
    company = models.ForeignKey('job_poster.company_name', max_length =50, blank=True, on_delete=models.CASCADE)
    zip_code = models.ForeignKey('job_poster.zip_code', max_length =50, blank=True)
    description = models.CharField(max_length =500, blank=True)
    start_date = models.DateField( null=True, blank=True)
    end_date = models.DateField( null=True, blank=True)


    def __str__(self):
        return self.job_title