from django.shortcuts import render, redirect
from polls.views.Class.Charge import Charge


def charge(request):
    if request.method == "GET":
        return render(request , "polls/charge.html")

    elif request.method == "POST":
        userid = request.POST.get("userid", None)
        money = request.POST.get("holder", None)
        if money.isdigit():
            Charge.charge_money(userid, money)
            params = {"msg": "チャージが完了しました。"}
            return render(request, "polls/charge.html", params)
        else:
            params = {"errmsg": "数字を入力して下さい。"}
            return render(request, "polls/charge.html", params)
