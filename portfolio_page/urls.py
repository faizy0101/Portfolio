from django.urls import path

from portfolio_page import views

urlpatterns = [
    path('', views.index, name='index'),
]