from django.contrib import admin
from .models import JobListings
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'company', 'zip_code','start_date', 'end_date')
    list_display_links = ('id', 'title')
    list_filter = ('company', )
    search_fields = ('title', 'description',  'zipcode', 'company')
    list_per_page = 25


admin.site.jobs(JobListings, ListingAdmin)