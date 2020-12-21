# チャージ履歴の取得

from django.shortcuts import render, redirect

from polls import models
from polls.views.Class.Charge import Charge


def chargehistory(request):
    # ログインしているか確認する
    if not "userid" in request.session:
        return redirect("/polls/login")

    if request.method == "GET":
        params = {"charge" : ""}
        try:
            userid = request.session["userid"]
            charge = Charge().get_chargehistory(userid)
            params["charge"] = charge
        except models.PollsCharginghistory.DoesNotExist as e:
            print(e)
    return render(request, "polls/chargeHistory.html", params)

