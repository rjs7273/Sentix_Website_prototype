import requests
from datetime import datetime
from .models import StockPrice

def fetch_stock_data(stock_code):
    """
    네이버 증권 API에서 일봉 데이터를 가져와 데이터베이스에 저장하는 함수
    """
    url = f"https://api.stock.naver.com/chart/domestic/item/{stock_code}/day"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for item in data:
            StockPrice.objects.update_or_create(
                stock_code=stock_code,
                local_date=datetime.strptime(item["localDate"], "%Y%m%d"),
                defaults={
                    "close_price": item["closePrice"],
                    "open_price": item["openPrice"],
                    "high_price": item["highPrice"],
                    "low_price": item["lowPrice"],
                    "volume": item["accumulatedTradingVolume"],
                },
            )
        print(f"{stock_code} 데이터 업데이트 완료!")
    else:
        print(f"데이터 가져오기 실패: {response.status_code}")

