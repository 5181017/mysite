from django.http import request
from django.shortcuts import render

from polls import models
from polls.views.Class.Cart import Cart


def cart(request):
    if request.method == "GET":
        userid = request.session["userid"]
        cart = Cart.get_cart(userid)
        request.session["cart"] = cart
        params = {"cart": cart}
        # Payページに遷移
        return render(request, "polls/cart.html", params)

    elif request.method == "POST":
        # 渡された値を取得
        productid = request.POST.get("productid", None)
        quantity = request.POST.get("quantity", None)
        userid = request.POST.get("userid", None)
        btn = request.POST.get("deletebtn", None)
        if "delete_btn" in btn:
            Cart.delete_cart(userid, productid)

        elif "pay_btn" in request.POST:
            # カートの更新
            Cart().update_cart(userid, productid, quantity)
            cart = Cart.get_cart(userid)
            request.session["cart"] = cart
            params = {"cart": cart}
            # Payページに遷移
            if "logo" in request.POST:
                return render(request, "polls/home.html", params)
            elif "cart" in request.POST:
                return render(request, "polls/cart.html", params)
            elif "sarch" in request.POST:
                return render(request, "polls/productList.html", params)
