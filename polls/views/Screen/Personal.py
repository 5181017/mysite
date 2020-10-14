from django.shortcuts import redirect, render

from polls.views.Class.User import User


def personal(request):
    # ログインしているか確認する
    if not request.session.exists("userid"):
        return redirect("/polls/login")

    if request.method == "GET":
        userid = request.session["userid"]
        user = User().get_user(userid)
        params = {
            "userName": user.values("name"),
            "address": user.values("address")
        }
        return render(request, "polls/personal.html", params)

    elif request.method == "POST":
        userid = request.session["userid"]
        new_user_name = request.POST.get["userName"]
        new_user_address = request.POST.get["address"]
        User().update_user(userid, new_user_name, new_user_address)
        return render(request, "polls/personal.html")
