from django.shortcuts import redirect, render

from polls.views.Class.Settlement import Settlement


def orderhistory(request):
    id = request.POST.get("userid", None)
    list = Settlement().get_settlement(id)
    # 前のページに遷移
    request.session["productlist"] = list
    params = {"productlist": list}
    return render(request, "polls/home.html", params)
