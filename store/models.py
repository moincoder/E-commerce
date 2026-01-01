from django.db import models
from ecommerce.models import BaseModel






class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug=models.SlugField(unique=True,null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(null=True,blank=True)
    discount=models.PositiveIntegerField(blank=True,null=True)
    catagory = models.ForeignKey('Catagory', on_delete=models.PROTECT, related_name='products')
    subcatagory=models.ForeignKey('SubCatagory',on_delete=models.PROTECT,related_name='subcatagory')

    def __str__(self):
        return self.name+' - '+self.stock.__str__()
    
    def save(self,*args,**kwargs):
        self.slug=self.name.lower().replace(' ','-')
        self.stock=5
        super().save(*args,**kwargs)





class productImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/products/')

    def __str__(self):
        return self.product.name




class Catagory(BaseModel):
    name = models.CharField(max_length=255)
    slug=models.SlugField(unique=True,blank=True,null=True)
    description = models.TextField()
    is_active=models.BooleanField(default=True)


    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.slug = self.name.lower().replace(' ', '-')
        super().save(*args, **kwargs)


class SubCatagory(BaseModel):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name='sub_catagories')
    name = models.CharField(max_length=255)
    slug=models.SlugField(null=True,blank=True)
    description = models.TextField()


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = self.name.lower().replace(' ', '-')
        super().save(*args, **kwargs)