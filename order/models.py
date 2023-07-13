from django.db import models
from users.models import UserModel
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.pk}"
    

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user  = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


