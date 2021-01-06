from django.shortcuts import redirect, render

from polls import models
from polls.views.Class.User import User


def personal(request):
    # ログインしているか確認する
    if not "userid" in request.session:
        return redirect("/polls/login")

    if request.method == "GET":
        try:
            userid = request.session["userid"]
            user = User().get_user(userid)
            name = user.name
        except Exception as e:
            print(e)
            return render(request , "polls/exception.html" , {"errorMsg" :"DB接続できませんでした。"})
        params = {
            "first_name" : name,
            "address" : user.address,
            "toast_flg" : "0"
        }


    elif request.method == "POST":
        userid = request.session["userid"]
        first_name = request.POST["first-name"]
        new_user_address = request.POST["address"]
        new_user_name = first_name

        params = {
            "msg": "",
            "first_name" : "",
            "address" : "",
            "toast_flg" : "0"
        }

        if not (new_user_name.isalnum() or new_user_address.isalnum()):
            params["msg"] = "特殊文字を使用しないでください"
            user = User().get_user(userid)
            params["first_name"] = first_name
            params["address"] = user.address
            return render(request, "polls/personal.html", params)

        User().update_user(userid, new_user_name, new_user_address)
        user = User().get_user(userid)
        params["address"] = user.address
        params["first_name"] = first_name
        params["toast_flg"] = "1"

    return render(request, "polls/personal.html", params)
