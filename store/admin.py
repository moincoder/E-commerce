from django.contrib import admin

# Register your models here.

from .models import Product, Catagory, productImage, SubCatagory


admin.site.register(Product)
admin.site.register(Catagory)   
admin.site.register(productImage)
admin.site.register(SubCatagory)
