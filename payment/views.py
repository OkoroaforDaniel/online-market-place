from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def pay(request, pk):
    return render(request, 'payment/pay.html')
