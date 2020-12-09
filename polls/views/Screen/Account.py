from django.db import DataError
from django.shortcuts import redirect, render

from polls import models
from polls.views.Class.User import User
from polls.views.Forms.UserForms import UserForm


def account(request):
    if request.method == "GET":
        return render(request, "polls/account.html" , {"form": UserForm()})

    elif request.method == "POST":
        userid = request.POST.get("userID", None)
        name = request.POST.get("name", None)
        pw = request.POST.get("pw", None)
        repw = request.POST.get("repassword", None)

        userForm = UserForm(request.POST)
        if not userForm.is_valid():
            print("バリデーションエラー:account()")
            return redirect("/polls/account")

        if pw == repw:
            try:
                User().register_user(userid, name, pw)
                user = User().auth(userid, pw)
                # 前のページに遷移
                request.session["userid"] = user.userID
                return redirect("/polls/home")
            except models.User.DoesNotExist as e:  # 登録できないエラー
                params = {"errmsg": "既にそのIDは存在しています"}
                print(e)
                return render(request, "polls/account.html", params)
            except DataError as e:
                print(e)
                params = {"errmsg": "長い"}
                return render(request , "polls/account.html" , params)
            except models.ValidationError as e:
                print(e)
                return redirect("/polls/login")
            except Exception as e:
                print(e)
                return render(request , "polls/exception.html" , {"errorMsg" :"DB接続できませんでした。"})

        else:
            params = {"errmsg": "再入力パスワードが違います"}
            print("パスワードが一致しません")
            return render(request, "polls/account.html", params)
