from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('pay/<int:pk>/', views.pay, name='pay'),
]
