from django.urls import path
from .views.Screen import Home, Cart, Charge, Review , ProductList, Account, ChargeHistory, Login, MyPage, \
    OrderHistory, Pay, Personal, ProductDetails

urlpatterns = [
    path("home", Home.home, name="home"),
    path("account", Account.account , name="account"),
    path("cart", Cart.cart, name="cart"),
    path("charge", Charge.charge, name="charge"),
    path("chargehistory", ChargeHistory.chargehistory, name="chargehistory"),
    path("productlist", ProductList.productlist, name="productlist"),
    # path("product", Common, name="common"),
    path("login", Login.login, name="login"),
    path("mypage", MyPage.mypage, name="mypage"),
    path("orderhistory", OrderHistory.orderhistory, name="orderhistory"),
    path("pay", Pay.pay, name="pay"),
    path("personal", Personal.personal, name="personal"),
    path("productdetails", ProductDetails.product_details, name="productdetails"),
    # path("<int:product_id>/review", Review, name="review")
]
