from ecommerce.models import BaseModel
from django.db import models
from store.models import Product
from accounts.models import User



class Cart(BaseModel):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user}"





class CartItem(BaseModel):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = [['cart', 'product']]
        ordering = ['-created_at']

    def total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity}x {self.product.name} in {self.cart}"
    