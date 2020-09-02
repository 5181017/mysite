# -登録ボタン-
# ユーザ登録(エラー表示)
from django.shortcuts import redirect, render

from polls import models
from polls.views.Class.User import User


def account(request):
    userid = request.POST.get("userid", None)
    name = request.POST.get("name", None)
    pw = request.POST.get("password", None)
    try:
        User().register_user(userid, name, pw)
        user = User().auth(userid, pw)
        # 前のページに遷移
        request.session["user"] = user
        params = {"user": user}
        return render(request, request.META['HTTP_REFERER'], params)
    except models.User.DoesNotExist:  # 登録できないエラー
        msg = "登録できませんでした"
        return msg
    except Exception:
        msg = "DBに接続できませんでした"
        return msg
