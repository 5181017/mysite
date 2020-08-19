from django.urls import path
from .views import Class


from . import views
from .views.Class import Cart
from .views.Class import Category
from .views.Class import Charge
from .views.Class import Product
from .views.Class import Review
from .views.Class import Settlement
from .views.Class import User

urlpatterns = [
    # path('', views.index, name='index'),
    path('/Cart', Cart, name='cart'),
    path('/Category', Category, name='category'),
    path('/Charge', Charge, name='Charge'),
    path('/Product', Product, name='Product'),
    path('/Review', Review, name='Review'),
    path('/Settlement', Settlement, name='Settlement'),
    path('/User', User, name='User'),
]