from django.shortcuts import render

from polls.views.Class.Product import Product
from polls.views.Class.Review import Review


def product_details(request, product_id):
    if "logo" in request.POST:
        return render(request, "polls/home.html")
    elif "cart" in request.POST:
        if not request.session.exists("userid"):
            param = {"ログインしてください。"}
            return render(request, "polls/login.html", param)
        return render(request, "polls/cart.html")
    elif "sarch" in request.POST:
        return render(request, "polls/productList.html")

    product = Product.get_product(product_id)
    review = Review.get_review(product_id)
    params = {
        "product": product,
        "review": review
    }
    return render(request, "polls/productDetails.html", params)

