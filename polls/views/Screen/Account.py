# -登録ボタン-
# ユーザ登録(エラー表示)


# 前のページに遷移



    elif request.method == "POST":
        userid = request.POST.get("userid", None)
        name = request.POST.get("name", None)
        pw = request.POST.get("password", None)
        repw = request.POST.get("repassword", None)

        p = {
            "userid" : request.POST.get()
        }
        if pw.equal(repw):
            try:
                User().register_user(userid, name, pw)
                user = User().auth(userid, pw)
                # 前のページに遷移
                request.session["userid"] = user.userid
                params = {"userid": userid}
                return render(request, "polls/home.html", params)
            except models.User.DoesNotExist:  # 登録できないエラー
                params = {"errmsg": "既にそのIDは存在しています"}
                return render(request, "polls/account.html", params)
            except Exception:
                params = {"errmsg": "DBに接続できませんでした"}
                return render(request, "polls/exception.html", params)
        else:
            params = {"errmsg": "再入力パスワードが違います"}
            return render(request, "polls/account.html", params)

