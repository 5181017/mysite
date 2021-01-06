from django.shortcuts import render, redirect

from polls import models
from polls.views.Class.Product import Product
from polls.views.Class.Settlement import Settlement


def payed(request):
    # ログインしているか確認する
    if not "userid" in request.session:
        return redirect("/polls/login")
    return render(request, "polls/payed.html", {"msg": "購入が完了しました"})
