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
        return render(request, "polls/cart.html", params)

    elif request.method == "POST":
        # 渡された値を取得
        productlist = request.POST.getlist("checkbox", None)
        userid = request.POST.get("userid", None)
        btn = request.POST.get("deletebtn", None)
        quantity = []
        for productid  in  productlist:
            quantity.append(request.POST.get(productid, None))

        if "delete_btn" in btn:
            Cart.delete_cart(userid, productlist)

        elif "pay_btn" in request.POST:
            # カートの更新
            for i in range(len(productlist)):
                Cart().update_cart(userid, productlist[i], quantity[i])
            cart = Cart.get_cart(userid)
            request.session["productid"] = cart.productid
            request.session["productid"] = cart.quantity

            params = {"cart": cart}
            # Payページに遷移
            if "logo" in request.POST:
                return render(request, "polls/home.html", params)
            elif "cart" in request.POST:
                return render(request, "polls/cart.html", params)
            elif "sarch" in request.POST:
                return render(request, "polls/productlist.html", params)
