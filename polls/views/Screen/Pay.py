from django.shortcuts import render

from polls.views.Class.Cart import Cart
from polls.views.Class.Product import Product


def pay(request):
    if request.method == "GET":
        userid = request.POST.get("userid", None)
        cart = Cart().get_cart(userid)
        for product in cart:
            data = Product().get_one_product(product.productid)
        request.session["productname"] = cart.productname
        # request.session["price"] = 
        params = {"cart": cart}
        return render(request, "polls/cart.html", params)

# -購入ボタン-
# カートから購入する商品を削除


# 購入処理
