# チャージ履歴の取得
from django.shortcuts import render, redirect
from polls.views.Class.Charge import Charge


def chargehistory(request):
    # ログインしているか確認する
    if not request.session.exists("userid"):
        return redirect("/polls/login")

    if request.method == "GET":
        userid = request.POST.get("userid", None)
        charge = Charge().get_chargehistory(userid)
        params = {"charge": charge}
        return render(request, "pools/chargeHistory.html", params)

    elif request.method == "POST":
        # 各ページに遷移
        if "logo" in request.POST:
            return render(request, "polls/home.html")
        elif "cart" in request.POST:
            return render(request, "polls/cart.html")
        elif "sarch" in request.POST:
            return render(request, "polls/productList.html")
