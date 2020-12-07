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
            name = user.name.split(" ")
            first_name , last_name = name[0] , name[1]

        except models.User.DoesNotExist as e:
            print(e)
            return redirect("/polls/exeption")
        except Exception as e:
            print(e)
            return redirect("/polls/exeption")
        params = {
            "first_name" : first_name,
            "last_name" : last_name,
            "address" : user.address,
            "toast_flg" : "0"
        }


    elif request.method == "POST":
        userid = request.session["userid"]
        first_name = request.POST["first-name"]
        last_name = request.POST["last-name"]
        new_user_address = request.POST["address"]
        new_user_name = first_name + " " + last_name

        params = {
            "msg": "",
            "first_name" : "",
            "last_name" : "",
            "address" : "",
            "toast_flg" : "0"
        }

        if not (new_user_name.isalnum() or new_user_address.isalnum()):
            params["msg"] = "特殊文字を使用しないでください"
            user = User().get_user(userid)
            name = user.name.split(" ")
            params["first_name"], params["last_name"] = name[0], name[1]
            params["address"] = user.address
            return render(request, "polls/personal.html", params)

        User().update_user(userid, new_user_name, new_user_address)
        user = User().get_user(userid)
        name = user.name.split(" ")
        params["address"] = user.address
        params["first_name"], params["last_name"] = name[0], name[1]
        params["toast_flg"] = "1"

    return render(request, "polls/personal.html", params)
