from django.shortcuts import render, redirect


def mypage(request):
    #ログインしているか確認する
    if not "userid" in request.session:
        return redirect("/polls/login")

    return render(request , "polls/mypage.html")