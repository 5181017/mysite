import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

from polls import models
from polls.views.Class.Cart import Cart
from polls.views.Class.Product import Product
from polls.views.Class.Review import Review


def product_details(request, product_id):
    if request.method == "GET":
        try:
            product = Product().get_one_product(product_id)
            review = Review().get_review(product_id)
            cnt = 0.0
            total = -1
            if len(review) != 0:
                for r in review:
                    cnt += r.reviewStar
                    print(cnt)
                total = round(cnt / len(review))

            satisfaction = {0 : "満足" , 1 : "普通" , 2 : "不満"}
            if total in satisfaction:
                satisfaction_str = satisfaction[total]
            else:
                satisfaction_str = "まだ評価されていません"
            params = {
                "product": product,
                "review": review,
                "total_review" : satisfaction_str,
                "productIdList" : ""
            }
            if "userid" in request.session:
                userid =request.session["userid"]
                cart = Cart().get_cart(userid)
                productIdList = []
                for c in cart:
                    productIdList.append(c.productID.productID)
                params.update({"productIdList": productIdList})

            return render(request, "polls/productDetails.html", params)
        except models.User.DoesNotExist as e:
            print(e)
            return redirect("/polls/exception" , "あなたのアカウントがありません")
        except Exception as e:
            print(e)
            return render(request , "polls/exception.html" , {"errorMsg" :"DB接続できませんでした。"})



    # if request.method == "POST":
    #     userid = request.session["userid"]
    #     productid = request.POST["productid"]
    #     Cart().insert_cart(userid , productid , 1)
    #     return redirect("/polls/productDetails/" + productid)

def re_order(request):
    userid = request.session["userid"]
    Cart().insert_cart(userid, request.GET["product_id"], 1)
    content = json.dumps({"result": "success"})  # 仮データ
    return HttpResponse(content)
