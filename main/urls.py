from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('outlets', views.outlets, name='outlets'),
    path('logout', views.logout, name='logout'),
    path('dishes', views.dishes, name='dishes'),
    path('addDish', views.addDish, name='addDish'),
    path('addOutlet', views.addOutlet, name='addOutlet'),
    path('pos', views.pos, name='pos'),
    path('bill', views.bill, name='bill'),
    path('test', views.test, name='test')
]
