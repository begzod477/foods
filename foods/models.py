from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=75, verbose_name='kategoriya nomi')

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=77, verbose_name='ovqat nomi')
    description = models.TextField(null=True, blank=True, verbose_name='ovqat haqida')
    price = models.IntegerField(verbose_name='ovqat narxi')
    is_aviable = models.BooleanField(default=True, verbose_name='mavjudligi')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Foods', verbose_name='qaysi kategoriyaga tegishliligi')

    def __str__(self):
        return self.name

class Orders(models.Model):
    customer_name = models.CharField(max_length=22, verbose_name='buyurtmachi nomi')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="orders", verbose_name='qaysi ovqatga buyurtmai')
    quantity = models.PositiveIntegerField(verbose_name='miqdori')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='buyurtma vaqti')

    def __str__(self):
        return self.customer_name

