from django.core.management.base import BaseCommand
from sec_api import MappingApi 
from edgar_data.models import Company

class Command(BaseCommand):
    help = 'Populates the database with company details using SEC API'

    def handle(self, *args, **kwargs):
        api_key = '880e695a62b65a8ed6191eeb3650f3e219f99eede29037143bd41ed6369db07d'
        mapping_api = MappingApi(api_key=api_key)

        tickers = ['TSLA', 'GOOG', 'NVDA', 'MSFT']  # Example tickers, you can expand this list

        for ticker in tickers:
            try:
                results = mapping_api.resolve('ticker', f'^{ticker}$')

                if results:
                    for company_data in results:
                        Company.objects.update_or_create(
                            ticker=company_data['ticker'],
                            defaults={
                                'name': company_data['name'],
                                'cik': company_data['cik'],
                                'cusip': company_data['cusip'],
                                'exchange': company_data['exchange'],
                                'category': company_data['category'],
                                'sector': company_data.get('sector'),
                                'industry': company_data.get('industry'),
                                'sic': company_data.get('sic'),
                                'sic_sector': company_data.get('sicSector'),
                                'sic_industry': company_data.get('sicIndustry'),
                                'fama_sector': company_data.get('famaSector'),
                                'fama_industry': company_data.get('famaIndustry'),
                                'currency': company_data['currency'],
                                'location': company_data.get('location'),
                                'external_id': company_data['id'],
                            }
                        )
                self.stdout.write(self.style.SUCCESS(f'Successfully populated data for ticker {ticker}'))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error fetching data for {ticker}: {str(e)}'))

