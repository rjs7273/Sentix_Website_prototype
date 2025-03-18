from django.core.management.base import BaseCommand
from stocks.data_fetch import fetch_stock_data

class Command(BaseCommand):
    help = "네이버 증권 데이터를 가져와 데이터베이스에 저장합니다."

    def handle(self, *args, **kwargs):
        stock_code = "005930"  # 삼성전자 (필요 시 다른 종목 코드 추가 가능)
        fetch_stock_data(stock_code)
        self.stdout.write(self.style.SUCCESS(f"{stock_code} 데이터 저장 완료!"))
