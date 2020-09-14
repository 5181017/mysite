from django.shortcuts import render


def mypage(request):
    if request.method == 'POST':
        # ホーム画面(1)
        if 'button_1' in request.POST:
            return render(request, "polls/Home.html")
        # 商品一覧ページ (2)
        elif 'button_2' in request.POST:
            SearchWord = request.POST.get("searchword")
            return render(request, "polls/ProductList.html", SearchWord)
        # -チャージ-(09画面に遷移)
        elif 'button_11' in request.POST:
            return render(request, "polls/ChargeHistory.html")
        # -注文履歴-(12画面に遷移)
        elif 'button_12' in request.POST:
            return render(request, "polls/OrderHistory.html")
        # -個人情報変更-(11画面に遷移)
        elif 'button_9' in request.POST:
            return render(request, "polls/Pasonal.html")
        # -チャージ履歴-(13画面に遷移)
        elif 'button_13' in request.POST:
            return render(request, "polls/ChargeHistory.html")
