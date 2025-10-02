from django.urls import path
from . import views

urlpatterns = [
    path('', views.credit_simulator, name='credit_simulator'),
]
