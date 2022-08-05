from django.contrib import admin
from .models import products

class productsAdmin(admin.ModelAdmin):
    list_display = ('name','price')


# Register your models here.
admin.site.register(products,productsAdmin)
