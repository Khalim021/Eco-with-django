from django.urls import path

from api.views import ProductListAPIView, ProductRetrieveAPIView

app_name = 'api'

urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view()),
]




