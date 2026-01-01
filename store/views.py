from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from store.models import Product

# Create your views here.


# def Products():
#     return render(request,'products/product.html')



class ProductsView(ListView):
    template_name='products/product.html'
    model=Product
    context_object_name='products'



# class ProductDetailView(DetailView):
#     model=Product
#     template_name='products/product_details.html'
#     context_object_name='product'


def ProductDetailView(request):
    return render(request,'products/product_detail.html')