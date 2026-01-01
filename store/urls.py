from . import views
from django.urls import path


urlpatterns = [
    path('',views.ProductsView.as_view(), name='products'),
    path('product-detail/',views.ProductDetailView, name='product_detail'),
]