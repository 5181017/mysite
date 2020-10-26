from django.shortcuts import render, redirect

from polls.views.Class.Cart import Cart
from polls.views.Class.Product import Product


def cart(request):
    #ログインしているか確認する
    if not request.session.exists("userid"):
        return redirect("/polls/login")

    if request.method == "GET":

        if 'userid' in request.session:
            userid = request.session["userid"]
            cart = Cart.get_cart(userid)
            params = {"cart": cart}


            userid = request.session["userid"]
            urlList = []
            priceList = []
            nameList = []
            cartList = Cart.get_cart(userid)

            list = [] #追加
            # この段階で画像、商品名、値段が必要
            for proId in cartList.values("productID"):
                urlList.append(Product.get_imageurl(proId))
                priceList.append(Product.get_price(proId))
                nameList.append(Product.get_one_product(proId).productName)

                list = [Product.get_imageurl(proId) , Product.get_price(proId) ,Product.get_one_product(proId).productName] #追加
            # params = {
            #     "urlList": urlList,
            #     "priceList": priceList,
            #     "nameList": nameList
            # }
            params = {"list" : list} #追加
        else:
            params = {}
        return render(request, "polls/cart.html", params)

    elif request.method == "POST":
        # 値を取得
        buylist = request.POST.getlist("checkbox", None)
        userid = request.POST.get("userid", None)
        btn = request.POST.get("delete_btn", None)
        quantity = []
        for productid in buylist:
            quantity.append(request.POST.get(productid, None))

        if "delete_btn" in btn:
            Cart.delete_cart(userid, btn)

        elif "pay_btn" in request.POST:
            # カートの更新
            for i in range(len(buylist)):
                Cart().update_cart(userid, buylist[i], quantity[i])
            cartlist = Cart.get_cart(userid)
            request.session["buylist"] = buylist
            params = {
                "cart": cartlist,
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
            param = {request.POST.get("searchWord")}
            return render(request, "polls/productList.html", param)
