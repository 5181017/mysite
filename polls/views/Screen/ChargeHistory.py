# チャージ履歴の取得
from django.shortcuts import redirect

from polls.views.Class.Charge import Charge


def chargehistory(request):
    if request.method == "GET":
        return redirect("pools/chargehistory.html")

    elif request.method == "POST":
        userid = request.POST.get("userid", None)
        Charge().get_chargehistory(userid)
