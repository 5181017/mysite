import re

from django.shortcuts import render, redirect

from polls import models
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
        productid = request.POST["productid"]
        title = request.POST["title"]
        comment = request.POST["commnet"]
        review = request.POST["review"]
        user_id = request.session['userid']  # useridだけをとる
        product = Product().get_one_product(productid)
        params = {
            "review": review,
            "product": product,
            "title": title,
            "comment": comment,
        }
        check_comment = re.sub("。|、|（|）" , "" , str(comment))
        if not check_comment.isalnum() and not check_comment.isalpha():
            params["msg"] = "特殊文字を使用しないでください"
            return render(request , "polls/review.html" , params)
        try:
            reviewid = ("000" + user_id + productid + str(datetime.datetime.today().strftime("%M%S")))[-10:]
            rv.register_review(reviewid ,user_id , productid , review, title, comment)
        except models.Review.DoesNotExist as e:
            print(e)
            return render(request, 'polls/review.html', params)
        except BaseException as e:
            print(e)
            params["title_msg"] = "文字数上限は50文字です"
            return render(request, 'polls/review.html', params)
        return redirect("/polls/productDetails/" + productid)
