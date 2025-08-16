
from django.contrib import admin
from .models import Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=("id","name","category","bank")
    search_fields=("name","category","bank")
