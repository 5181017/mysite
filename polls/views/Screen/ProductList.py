from django.shortcuts import render

from polls.views.Class.Product import Product


# 商品のインスタンスを渡す　セッション
def productlist(request):
    category=request.GET.get("category", None)
    # if category 条件
    product = Product().get_product(category)
    request.session["product"] = product
    params = {"product": product}
    return render(request, "polls/productlist.html", params)
