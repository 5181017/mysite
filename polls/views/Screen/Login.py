from django.shortcuts import redirect, render

from polls import models
from polls.views.Class.User import User


def login(request):
    if request.method == "GET":
        return render(request, "polls/login.html")

    elif request.method == "POST":
        userid = request.POST.get("id", None)
        pw = request.POST.get("pw", None)
        if "login_btn" in request.POST:
            return redirect("/polls/home")
        try:
            user = User().auth(userid, pw)
            if 'userid' in request.session:
                print("useridセッションが既にあります")
                return redirect("/polls/home")
            request.session["userid"] = user.userID
            print("useridセッション作成")
            return redirect("/polls/home")

        except models.User.DoesNotExist:  # 登録できないエラー
            params = {"errmsg": "ユーザーIDが違います。"}
            return render(request, "polls/login.html", params)
        except Exception:
            params = {"errmsg": "DBに接続できませんでした"}
            return render(request, "polls/exception.html", params)
