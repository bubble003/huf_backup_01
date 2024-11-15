from django.contrib import admin
import donation.models
from .models import donation_table

admin.site.register(donation_table)
