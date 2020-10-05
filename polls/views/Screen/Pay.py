from django.shortcuts import render

from polls.views.Class.Product import Product
from polls.views.Class.Settlement import Settlement


def pay(request):
    if request.method == "GET":
        buylist = request.POST.get("buylist", None)    # 購入商品IDリスト
        buypro = []                                    # 購入商品リスト
        quantity = request.POST.get("quantity", None)  # 購入商品個数リスト
        total = 0                                      # 合計金額
        price = []                                     # 値段
        i = 0
        for buyid in buylist:
            buypro.append(Product().get_one_product(buyid))

        # 合計金額の計算 total
        for proId in buylist:
            total = total + Product().get_price(proId) * quantity[i]
            price = Product().get_price(proId) * quantity[i]
            i += 1

        params = {
            "total": total,
            "price": price,
            "buyproList": buypro
        }

        return render(request, "polls/cart.html", params)

    elif request.method == "POST":
        userId = request.POST.get("userid", None)      # userID
        buyList = request.POST.get("buylist", None)    # 購入商品IDリスト
        total = request.POST.get("total", None)        # 合計金額
        # 購入処理
        if Settlement().get_remaining_money(userId, total):
            Settlement.buy(total, userId, buyList)
            return render(request, "polls/home.html")
        else:
            errmsg = "残高が足りません。チャージしてください。"
            params = {"errmsg": errmsg}
            return render(request, "polls/charge.html", params)
