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
        first_name = request.POST["first-name"]
        last_name = request.POST["last-name"]
        new_user_address = request.POST["address"]
        new_user_name = first_name + " " + last_name

        #ここから
        if not new_user_name.isalnum() or not new_user_address.isalnum():
            params = {
                "msg" : "特殊文字を使用しないでください"
            }
            return render(request, "polls/personal.html" , params)
        User().update_user(userid, new_user_name, new_user_address)
        user = User().get_user(userid)
        params = {"user" : user}

    return render(request, "polls/personal.html", params)
