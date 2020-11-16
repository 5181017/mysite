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
        except models.User.DoesNotExist as e:
            print(e)
            return redirect("/polls/exeption")
        except Exception as e:
            print(e)
            return redirect("/polls/exeption")
        params = {
            "user" : user
        }


    elif request.method == "POST":
        userid = request.session["userid"]
        new_user_name = request.POST["userName"]
        new_user_address = request.POST["address"]
        User().update_user(userid, new_user_name, new_user_address)
        user = User().get_user(userid)
        params = {"user" : user}

    return render(request, "polls/personal.html", params)
