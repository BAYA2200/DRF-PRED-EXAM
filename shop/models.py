from django.db import models

# Create your models here.
from account.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f" Категория {self.name}"

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category} название {self.name} Цена {self.price}  ПРОДАВЕЦ {self.profile}"



class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"название {self.item} количество{self.quantity}   покупатель {self.profile}"



