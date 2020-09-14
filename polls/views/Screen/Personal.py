from django.shortcuts import redirect, render

from polls.views.Class.User import User


def personal(request):
    user_obj = User.get_user(request.session["user_id"])
    if request.method == "GET":
        params = {
            "user" : user_obj
        }
        return render(request , "polls/personal.html" , params)

    elif request.method == "POST":
        new_user_name = request.POST.get["userName"]
        new_user_address = request.POST.get["address"]
        user = User()
        user.update_user(new_user_name , new_user_address)
        return redirect("mypage")