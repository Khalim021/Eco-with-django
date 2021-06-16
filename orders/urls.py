from django.urls import path

from orders.views import OrderCreateView, OrderHistoryListView

app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create'),
    path('history/', OrderHistoryListView.as_view(), name='history'),
]
