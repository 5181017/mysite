from django.urls import path
from .views.Screen import Home, Cart, Charge, Review, ProductList, Account, ChargeHistory, Login, MyPage, \
    OrderHistory, Pay, Personal, ProductDetails, Payed

urlpatterns = [
    path("account", Account.account, name="account"),
    path("cart", Cart.cart, name="cart"),
    path("charge", Charge.charge, name="charge"),
    path("ajaxCharge" , Charge.ajaxCharge , name="ajaxCharge"),
    path("chargeHistory", ChargeHistory.chargehistory, name="chargeHistory"),
    path("home", Home.home, name="home"),
    path("payed", Payed.payed, name="payed"),
    path("login", Login.login,name="login"),
    path("orderHistory", OrderHistory.orderhistory, name="orderHistory"),
    path("pay", Pay.pay, name="pay"),
    path("personal", Personal.personal, name="personal"),
    # path("productList", ProductList.productlist, name="productList"),
    path("review/<str:product_id>", Review.review , name="review"),
    path("myPage", MyPage.mypage, name="myPage"),  # htmlない
    path("productDetails/<str:product_id>", ProductDetails.product_details, name="productDetails"),
    path("reorder" , ProductDetails.re_order , name="reOrder"),
    path("logout" , Home.logout , name="logout"),
    # path("exception" ,  , name="exception")
]
