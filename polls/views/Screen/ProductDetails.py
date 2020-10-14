from django.shortcuts import render, redirect

from polls import models
from polls.views.Class.Product import Product
from polls.views.Class.Review import Review


def product_details(request, product_id):
    # if "logo" in request.POST:
    #     return render(request, "polls/home.html")
    # elif "cart" in request.POST:
    #     if not request.session.exists("userid"):
    #         param = {"ログインしてください。"}
    #         return render(request, "polls/login.html", param)
    #     return render(request, "polls/cart.html")
    # elif "sarch" in request.POST:
    #     return render(request, "polls/productList.html")
    try:
        product = Product.get_one_product(product_id)
        review = Review.get_review(product_id)
    except models.User.DoesNotExist | Exception:
        return redirect("/polls/exception")
    params = {
        "product": product,
        "review": review
    }
    return render(request, "polls/productDetails.html", params)

