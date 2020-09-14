from django.shortcuts import render

from polls.views.Class.Product import Product
from polls.views.Class.Settlement import Settlement


def pay(request):
    if request.method == "GET":
        buylist = request.POST.get("buylist", None)  # 購入商品IDリスト
        buypro = []  # 購入商品リスト
        quantity = request.POST.get("quantity", None)  # 購入商品個数リスト
        total = 0
        price = []
        i = 0
        for buyid in buylist:
            buypro.append(Product().get_one_product(buyid))

        # 合計金額の計算 total
        for id in buylist:
            total = total + Product().get_price(id) * quantity[i]
            price = Product().get_price(id) * quantity[i]
            i += 1

        params = {
            "total": total,
            "price": price,
            "buyprolist": buypro
        }

        return render(request, "polls/cart.html", params)

    elif request.method == "POST":
        userid = request.POST.get("userid", None)
        buylist = request.POST.get("buylist", None)  # 購入商品IDリスト
        buypro = []  # 購入商品リスト
        total = request.POST.get("total", None)
        for buyid in buylist:
            buypro.append(Product().get_one_product(buyid))
        # 購入処理
        if Settlement().get_remaining_money(userid, total):
            Settlement.buy(total, userid, buylist)
            return render(request, "polls/home.html")
        else:
            errmsg = "残高が足りません。チャージしてください。"
            params = {"errmsg": errmsg}
            return render(request, "polls/charge.html", params)
