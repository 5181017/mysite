from django.shortcuts import render, redirect

from polls.views.Class.Product import Product
from polls.views.Class.Settlement import Settlement


def pay(request):
    # ログインしているか確認する
    if not request.session.exists("userid"):
        return redirect("/polls/login")

    # userId = request.POST.get("userid", None)      # userID
    userId = request.session["userid"]
    buyList = request.POST.getlist("buylist")    # 購入商品IDリスト
    total = request.POST["total_money"]        # 合計金額

    print(request.POST)

    # 購入処理
    if Settlement().get_remaining_money(userId, total):
        Settlement().buy(total, userId, buyList)
        return redirect("/polls/home")
    else:
        errmsg = "残高が足りません。チャージしてください。"
        params = {"errmsg": errmsg}
        return render(request, "polls/charge.html", params)
