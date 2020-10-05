from django.urls import path
from .views.Screen import Home, Cart, Charge, Review, ProductList, Account, ChargeHistory, Login, MyPage, \
    OrderHistory, Pay, Personal, ProductDetails

urlpatterns = [
    path("account", Account.account, name="account"),
    path("cart", Cart.cart, name="cart"),
    path("charge", Charge.charge, name="charge"),
    path("chargeHistory", ChargeHistory.chargehistory, name="chargeHistory"),
    path("home", Home.home, name="home"),
    path("login", Login.login, name="login"),
    path("orderHistory", OrderHistory.orderhistory, name="orderHistory"),
    path("pay", Pay.pay, name="pay"),
    path("personal", Personal.personal, name="personal"),
    # path("productList", ProductList.productlist, name="productList"), # いらない
    # path("<int:product_id>/review", Review, name="review"),
    path("myPage", MyPage.mypage, name="myPage"),  # htmlない
    path("productDetails", ProductDetails.product_details, name="productDetails")  # htmlない
]
