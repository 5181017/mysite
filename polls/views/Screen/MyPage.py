from django.shortcuts import render


def mypage(request):
    if request.method == 'POST':
        # -ホーム-
        if "logo" in request.POST:
            return render(request, "polls/Home.html")
        # -商品一覧-
        elif "sarch" in request.POST:
            param = {request.POST.get("searchWord")}
            return render(request, "polls/ProductList.html", param)
        # -カート-
        elif "cart" in request.POST:
            return render(request, "polls/cart.html")
        # -チャージ-(09画面に遷移)
        elif "cha_btn" in request.POST:
            return render(request, "polls/charge.html")
        # -注文履歴-(12画面に遷移)
        elif "ordHis_btn" in request.POST:
            return render(request, "polls/orderHistory.html")
        # -個人情報変更-(11画面に遷移)
        elif "per_btn" in request.POST:
            return render(request, "polls/personal.html")
        # -チャージ履歴-(13画面に遷移)
        elif "chaHis_btn" in request.POST:
            return render(request, "polls/chargeHistory.html")
