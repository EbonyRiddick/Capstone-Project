from django.contrib import admin
from .models import JobListings
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_title',  'company_name', 'zip_code','start_date', 'end_date')
    list_display_links = ('id', 'job_title')
    list_filter = ('company_name', )
    search_fields = ('job_title','zip_code', 'company_name')
    list_per_page = 25


admin.site.register(JobListings, ListingAdmin)