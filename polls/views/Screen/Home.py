from django.shortcuts import render, redirect

from polls import models
from polls.views.Class.Category import Category


# カテゴリのインスタンスを渡す セッション
from polls.views.Class.Product import Product


def home(request):
    # ログインしているユーザ（テスト用）
    request.session['userid'] = "1"

    try:
        if request.method == "GET":
            category = Category().get_category()
            param = {"category": category}
            return render(request, "polls/home.html", param)

        if request.method == "POST":
            product = ""
            category = Category().get_category()
            print(request.POST)
            if "category_btn" in request.POST:
                btn = request.POST.get("category_btn", None)
                product = Product().get_product(btn)

            elif "search_btn" in request.POST:
                text = request.POST.get("search")
                product = Product().get_find(text)
                print(text)
                print(request.POST)
                print("lakjfd;lkajds;flajsdflj")

            param = {
                "product": product,
                "category": category
            }


        return render(request, "polls/productList.html", param)
    except models.Products.DoesNotExist:
        return render(request , "polls/exception.html" , "商品が見つかりませんでした。")
    except Exception:
        return render(request , "polls/exception.html" , "DB接続できませんでした。")


