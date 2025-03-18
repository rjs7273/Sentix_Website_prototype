from django.contrib import admin
from .models import StockPrice

@admin.register(StockPrice)
class StockPriceAdmin(admin.ModelAdmin):
    list_display = ('stock_code', 'local_date', 'close_price', 'open_price', 'high_price', 'low_price', 'volume')
    search_fields = ('stock_code', 'local_date')

