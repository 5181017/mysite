from django.shortcuts import render, redirect
from polls.views.Class.Charge import Charge
from polls.views.Class.User import User


def charge(request):
    # ログインしているか確認する
    if not "userid" in request.session:
        return redirect("/polls/login")

    if request.method == "GET":
        return render(request , "polls/charge.html")

    elif request.method == "POST":
        userid = request.session["userid"]
        money = request.POST["holder"]
        if money.isdigit():
            User().charge_money(userid, int(money))
            params = {"msg": "チャージが完了しました。"}
            return render(request, "polls/charge.html", params)
        else:
            params = {"errmsg": "数字を入力して下さい。"}
            return render(request, "polls/charge.html", params)
