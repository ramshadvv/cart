from django.http import HttpResponse
from django.shortcuts import render
from .models import products

# Create your views here.
def f_product(request):
    item = products.objects.all()
    return render(request,'product.html',{'products' : item})
