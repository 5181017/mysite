# -チャージボタン-
# チャージ(数字チェック)
from django.shortcuts import render, redirect
from polls.views.Class.Charge import Charge


def charge(request):
    if request.method == "GET":
        return redirect("pools/charge.html")

    elif request.method == "POST":
        userid = request.POST.get("userid", None)
        money = request.POST.get("money", None)
        if money.isdigit():
            Charge.charge_money(userid, money)
        else:
            params = {"errmsg": "数字を入力して下さい。"}
            return render(request, "polls/charge.html", params)
