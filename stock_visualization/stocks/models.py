from django.db import models

class StockPrice(models.Model):
    stock_code = models.CharField(max_length=10)  # 종목 코드 (예: 005930)
    local_date = models.DateField()               # 날짜
    close_price = models.IntegerField()           # 종가
    open_price = models.IntegerField()            # 시가
    high_price = models.IntegerField()            # 최고가
    low_price = models.IntegerField()             # 최저가
    volume = models.BigIntegerField()             # 거래량

    def __str__(self):
        return f"{self.stock_code} - {self.local_date}"
