from django.shortcuts import render

from polls.views.Class.Product import Product

# 商品のインスタンスを渡す　セッション
# def productlist(request):
# print("GET_productList")
# category = request.GET.get("sarchCategory", None)
# product = Product().get_product(category)
# request.session["product"] = product
# params = {"product": product}
# return render(request, "polls/productList.html", params)
