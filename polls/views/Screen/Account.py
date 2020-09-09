from django.shortcuts import redirect, render
from polls.views.Class import User
# -登録ボタン-

# ユーザ登録(エラー表示)
def account(request):
    if request.method == 'GET':
        #要求
        return redirect(request,'05')
    elif request.method == 'POST':
        #送信
        userID               = request.POST['userID']
        name                 = request.POST['name']
        pw                   = request.POST['pw']
        passwordConfirmation = request.Post['passwordConfirmaion']

        if(Check(pw,passwordConfirmation)):
            User.register_user(userID,name,pw)
            return render(request,'01')
        else:
            params = {
                "userID": userID,
                "name"  : name,
                "pw"    : pw,
            }
            return render(request,'05',params)


# 前のページに遷移
    return redirect(request.META['HTTP_REFERER'])

# -登録済みの人ボタン-
# 06画面に遷移
    return redirect(request,'06')

#パスワードの確認
def Check(pw,passwordConfirmation):
    checkresult = False
    if(pw == passwordConfirmation):
        checkresult = True
    return  checkresult