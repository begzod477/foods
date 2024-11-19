from django.contrib import admin

# Register your models here.

from .models import Food, Category, Orders

admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Orders)