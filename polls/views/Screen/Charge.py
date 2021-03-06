import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from polls.views.Class.Charge import Charge
from polls.views.Class.User import User



def charge(request):
    # ログインしているか確認する
    if not "userid" in request.session:
        return redirect("/polls/login")

    if request.method == "GET":
        return render(request , "polls/charge.html", {"num": 0})

    # elif request.method == "POST":
    #     userid = request.session["userid"]
    #     money = request.POST["holder"]
    #     if money.isdigit():
    #         User().charge_money(userid, int(money))
    #         params = {"msg": "チャージが完了しました。"}
    #         return render(request, "polls/charge.html", params)
    #     else:
    #         params = {"errmsg": "数字を入力して下さい。"}
    #         return render(request, "polls/charge.html", params)

def ajaxCharge(request):
    userid = request.session["userid"]
    money = request.GET["money"]

    if money.isdigit():
        User().charge_money(userid, int(money))
        request.session["money"] = User().get_user(userid).money
        content = json.dumps({
            "msg" : "チャージが完了しました。",
            "money" : request.session["money"],
            "flg" : True
        })
    else:
        content = json.dumps({
            "msg": "数字を入力して下さい。",
            "flg" : False
        })
    return HttpResponse(content)