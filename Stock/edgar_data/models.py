from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    ticker = models.CharField(max_length=10, unique=True, default='Unknown')
    cik = models.CharField(max_length=10, unique=True)
    cusip = models.CharField(max_length=20, unique=True, null=True, blank=True)
    exchange = models.CharField(max_length=20, default='Unknown')
    category = models.CharField(max_length=50)
    sector = models.CharField(max_length=50, null=True, blank=True, default='Unknown')  # Default to 'Unknown'
    industry = models.CharField(max_length=100, null=True, blank=True, default='Unknown')  # Default to 'Unknown'
    sic = models.CharField(max_length=10, null=True, blank=True, default='0000')  # Default to a placeholder value
    sic_sector = models.CharField(max_length=50, null=True, blank=True, default='Unknown')  # Default to 'Unknown'
    sic_industry = models.CharField(max_length=100, null=True, blank=True, default='Unknown')  # Default to 'Unknown'
    fama_sector = models.CharField(max_length=50, null=True, blank=True, default='Unknown')  # Default to 'Unknown'
    fama_industry = models.CharField(max_length=100, null=True, blank=True, default='Unknown')  # Default to 'Unknown'
    currency = models.CharField(max_length=10, default="USD")  # USD is a reasonable default
    location = models.CharField(max_length=255, null=True, blank=True, default='Not Specified')  # Default to 'Not Specified'
    external_id = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.ticker})"
    
class Filing(models.Model):
    file_date = models.CharField(max_length=15)
    file_type = models.CharField(max_length=8)

    def __str__(self):
        return 