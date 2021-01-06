from django.shortcuts import redirect, render

from polls import models
from polls.views.Class.User import User
from polls.views.Forms.LoginForm import LoginForm


def login(request):
    if request.method == "GET":
        return render(request, "polls/login.html", {"form" : LoginForm})

    elif request.method == "POST":
        userid = request.POST.get("userID", None)
        pw = request.POST.get("pw", None)
        login_form = LoginForm(request.POST)

        if not login_form.is_valid():
            print("バリデーションエラー:login()")
            print(login_form.errors)

        try:
            user = User().auth(userid, pw)
            request.session["userid"] = user.userID
            return redirect("/polls/home")
        except models.User.DoesNotExist as e:  # 登録できないエラー
            print(e)
            params = {"errmsg": "ユーザーIDが違います。"}
            return render(request, "polls/login.html", params)
        except Exception as e:
            print(e)
            return render(request, "polls/exception.html", {"errorMsg": "DB接続できませんでした。"})
