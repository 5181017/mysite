from django.shortcuts import render, redirect

from polls.views.Class.Product import Product
from polls.views.Class.Review import Review
import datetime

def review(request, product_id):
    # ログインしているか確認する
    if not "userid" in request.session:
        return redirect("/polls/login")

    # TODO画像を載せる
    if request.method == "GET":

        product = Product().get_one_product(product_id)

        params = {
            "product": product
        }
        return render(request, 'polls/review.html', params)
    elif request.method == "POST":
        rv = Review()
        reviewstar = 4
        productid = request.POST["productid"]
        title = request.POST["title"]
        comment = request.POST["commnet"]
        user_id = request.session['userid']  # useridだけをとる
        reviewid = ("000" + user_id + productid + str(datetime.datetime.today().strftime("%M%S")))[-10:]
        rv.register_review(reviewid ,user_id , productid , reviewstar, title, comment)
        return redirect("/polls/productDetails/" + productid)
