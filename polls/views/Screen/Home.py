from django.shortcuts import render, redirect

from polls.views.Class.Category import Category


# カテゴリのインスタンスを渡す セッション
from polls.views.Class.Product import Product


def home(request):
    # ログインしているユーザ（テスト用）
    request.session['userid'] = "1"


    if request.method == "GET":
        category = Category().get_category()
        param = {"category": category}
        return render(request, "polls/home.html", param)

    if request.method == "POST":
        btn = request.POST.get("category_btn", None)
        category = Category().get_category()
        if "category_btn" in request.POST:
            product = Product().get_product(btn)
            param = {
                "product": product,
                "sarchCategory": btn,
                "category": category
            }
            return render(request, "polls/productList.html", param)

        if "logo" in request.POST:
            return redirect("/polls/home")

        if "login" in request.POST:
            return redirect("/polls/login")

        if "cart" in request.POST:
            if not request.session.exists("userid"):
                return redirect("/polls/login")
            return render(request, "polls/cart.html")

        if "sarch" in request.POST:
            return render(request, "polls/productList.html")

    return redirect("/polls/home")
