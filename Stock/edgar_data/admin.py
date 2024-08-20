from django.contrib import admin

# Register your models here.
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'ticker', 
        'cik', 
        'cusip', 
        'exchange', 
        'sector', 
        'industry'
    )
    search_fields = ('name', 'ticker', 'cik', 'cusip', 'sector', 'industry')
    list_filter = ('exchange', 'sector', 'industry')
    ordering = ('name',)
    readonly_fields = ('external_id',)

    fieldsets = (
        (None, {
            'fields': ('name', 'ticker', 'cik', 'cusip', 'exchange', 'category', 'sector', 'industry', 'currency')
        }),
        ('Additional Information', {
            'classes': ('collapse',),
            'fields': ('sic', 'sic_sector', 'sic_industry', 'fama_sector', 'fama_industry', 'location', 'external_id')
        }),
    )

    def company_name_uppercase(self, obj):
        return obj.name.upper()
    company_name_uppercase.short_description = 'Company Name (Uppercase)'
