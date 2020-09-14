from django.http import request
from django.shortcuts import render

from polls import models
from polls.views.Class.Cart import Cart


def cart(request):
    if request.method == "GET":
        userid = request.session["userid"]
        cart = Cart.get_cart(userid)
        params = {"cart": cart}
        return render(request, "polls/cart.html", params)

    elif request.method == "POST":
        # 値を取得
        buylist = request.POST.getlist("checkbox", None)
        userid = request.POST.get("userid", None)
        btn = request.POST.get("deletebtn", None)
        quantity = []
        for productid in buylist:
            quantity.append(request.POST.get(productid, None))

        if "delete_btn" in btn:
            Cart.delete_cart(userid, buylist)  # TODO別のパラメータ？

        elif "pay_btn" in request.POST:
            # カートの更新
            for i in range(len(buylist)):
                Cart().update_cart(userid, buylist[i], quantity[i])
            cart = Cart.get_cart(userid)
            request.session["buylist"] = buylist
            params = {
                "cart": cart,
                "buylist": buylist,
                "quantity": quantity
            }
            return render(request, "polls/pay.html", params)
        # 各ページに遷移
        if "logo" in request.POST:
            return render(request, "polls/home.html")
        elif "cart" in request.POST:
            return render(request, "polls/cart.html")
        elif "sarch" in request.POST:
            return render(request, "polls/productlist.html")
