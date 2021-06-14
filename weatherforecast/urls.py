from django.urls import path
from weatherforecast import views

urlpatterns = [
    path('', views.index, name='home')
]