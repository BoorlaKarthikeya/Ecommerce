from django.shortcuts import render
from .models import *
def store(request):
	producs=Product.objects.all()
	context = {'products':producs,
	    'Profile' : request.user.username if request.user else 'Profile',
	    'user' : True if request.user.username else False,
	     }
	return render(request, 'store/store.html', context)

def cart(request):
	context = {}
	return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)