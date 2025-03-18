from django.shortcuts import render
from django.http import JsonResponse
from .models import StockPrice

def stock_chart_data(request, stock_code):
    """
    주어진 종목의 주가 데이터를 JSON으로 반환하는 API
    """
    data = StockPrice.objects.filter(stock_code=stock_code).order_by("local_date")

    json_data = [
        {
            "date": item.local_date.strftime("%Y-%m-%d"),
            "close_price": item.close_price
        }
        for item in data
    ]

    return JsonResponse(json_data, safe=False)

def chart_page(request):
    """
    차트 페이지를 렌더링하는 뷰
    """
    return render(request, "stocks/chart.html")
