from django.shortcuts import render, redirect

from polls.views.Class.Category import Category


# カテゴリのインスタンスを渡す セッション
def home(request):
    if request.method == "GET":
        category = Category().get_category()
        param = {"category": category}
        return render(request, "polls/home.html", param)

    if request.method == "POST":
        btn = request.POST.get("category_btn", None)
        if "category_btn" in btn:
            param = {"sarchCategory": btn}
            return render(request, "polls/productList.html", param)
        elif "logo" in request.POST:
            return render(request, "polls/home.html")
        elif "cart" in request.POST:
            if not request.session.exists("userid"):
                param = {"err": "ログインしてください。"}
                return render(request, "polls/login.html", param)
            return render(request, "polls/cart.html")
        elif "sarch" in request.POST:
            return render(request, "polls/productList.html")
    return redirect("pools.productList.html")
