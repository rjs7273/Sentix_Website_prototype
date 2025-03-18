from django.urls import path
from .views import stock_chart_data, chart_page

urlpatterns = [
    path("chart/<str:stock_code>/", stock_chart_data, name="stock_chart_data"),
    path("chart/", chart_page, name="chart_page"),
]
