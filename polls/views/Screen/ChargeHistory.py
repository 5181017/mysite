# チャージ履歴の取得
from django.shortcuts import render, redirect
from polls.views.Class.Charge import Charge


def chargehistory(request):
    # ログインしているか確認する
    if not "userid" in request.session:
        return redirect("/polls/login")

    if request.method == "GET":
        userid = request.session["userid"]
        charge = Charge().get_chargehistory(userid)
        params = {"charge": charge}
        return render(request, "polls/chargeHistory.html", params)

    elif request.method == "POST":
        # 各ページに遷移
        if "logo" in request.POST:
            return render(request, "polls/home.html")
        elif "cart" in request.POST:
            return render(request, "polls/cart.html")
        elif "search" in request.POST:
            return render(request, "polls/productList.html")
