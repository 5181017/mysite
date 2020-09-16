from django.shortcuts import redirect, render

from polls import models
from polls.views.Class.User import User


def account(request):
    if request.method == "GET":
        return render(request, "polls/account.html")

    elif request.method == "POST":
        userid = request.POST.get("userid", None)
        name = request.POST.get("name", None)
        pw = request.POST.get("password", None)
        repw = request.POST.get("repassword", None)

        if pw == repw:
            try:
                User().register_user(userid, name, pw)
                user = User().auth(userid, pw)
                # 前のページに遷移
                request.session["userid"] = user.values("userID").get()
                return redirect("/polls/home")
            except models.User.DoesNotExist:  # 登録できないエラー
                params = {"errmsg": "既にそのIDは存在しています"}
                return render(request, "polls/account.html", params)
            except Exception:
                params = {"errmsg": "DBに接続できませんでした"}
                return render(request, "polls/exception.html", params)
        else:
            params = {"errmsg": "再入力パスワードが違います"}
            return render(request, "polls/account.html", params)
