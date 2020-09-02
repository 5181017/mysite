from django.urls import path
from .views.Screen import Home, Cart, Charge, Review, Common, ProductList, Account, ChargeHistory, Login, MyPage, \
    OrderHistory, Pay, Personal, ProductDetails

urlpatterns = [
    path("home", Home.home, name="home"),
    path("account", Account.account, name="account"),
    path("cart", Cart.cart, name="cart"),
    path("charge", Charge, name="charge"),
    path("chargehistory", ChargeHistory, name="chargehistory"),
    path("productlist", ProductList.productlist, name="productlist"),
    path("product", Common, name="common"),
    path("login", Login, name="login"),
    path("mypage", MyPage, name="maypage"),
    path("orderhistory", OrderHistory, name="orderhistory"),
    path("pay", Pay, name="pay"),
    path("personal", Personal, name="personal"),
    path("productdetails", ProductDetails, name="productdetails"),
    path("review", Review, "review")
]
