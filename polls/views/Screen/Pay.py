from django.shortcuts import render, redirect

from polls import models
from polls.views.Class.Product import Product
from polls.views.Class.Settlement import Settlement
from polls.views.Class.User import User


def pay(request):
    # ログインしているか確認する
    if not "userid" in request.session:
        return redirect("/polls/login")

    # userId = request.POST.get("userid", None)      # userID
    userId = request.session["userid"]
    buyList = request.POST.getlist("buylist")    # 購入商品IDリスト
    total = request.POST["total_money"]        # 合計金額


    # 購入処理
    if Settlement().get_remaining_money(userId, total):
        Settlement().buy(total, userId, buyList)
        request.session["money"] = User().get_user(userId).money
        return redirect("/polls/payed")
    else:
        user = models.User.objects.get(userID=userId)
        mm = user.money
        errmsg = "残高が足りません。チャージしてください。"
        params = {"errmsg": errmsg, "num": int(total) - int(mm)}
        return render(request, "polls/charge.html", params)
