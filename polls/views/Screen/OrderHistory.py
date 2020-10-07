from django.shortcuts import render, redirect

from polls.views.Class.Settlement import Settlement


def orderhistory(request):
    # ログインしているか確認する
    if not request.session.exists("userid"):
        return redirect("/polls/login")

    if request.method == "GET":
        id = request.POST.get("userid", None)
        list = Settlement().get_settlement(id)
        # 前のページに遷移
        request.session["productlist"] = list
        params = {"productlist": list}
        return render(request, "polls/home.html", params)

    elif request.method == "POST":
        if "logo" in request.POST:
            return render(request, "polls/home.html")
        elif "cart" in request.POST:
            return render(request, "polls/cart.html")
        elif "sarch" in request.POST:
            param = {request.POST.get("searchWord")}
            return render(request, "polls/productList.html", param)
