from django.shortcuts import render, redirect

from polls import models
from polls.views.Class.Settlement import Settlement


def orderhistory(request):
    # ログインしているか確認する
    if not "userid" in request.session:
        return redirect("/polls/login")

    if request.method == "GET":
        id = request.session["userid"]
        try:
            list = Settlement().get_settlement(id)
            # 前のページに遷移
            params = {"productlist": list}
        except models.PayHistory.DoesNotExist:
            params = {"msg" : "履歴がありません"}
        except Exception as e:
            print(e)
            return redirect("/polls/exeption")
        return render(request, "polls/orderHistory.html", params)

    # elif request.method == "POST":
    #     if "logo" in request.POST:
    #         return render(request, "polls/home.html")
    #     elif "cart" in request.POST:
    #         return render(request, "polls/cart.html")
    #     elif "sarch" in request.POST:
    #         param = {request.POST.get("searchWord")}
    #         return render(request, "polls/productList.html", param)
