import re

from django.shortcuts import render, redirect

from polls import models
from polls.views.Class.Product import Product
from polls.views.Class.Review import Review
from polls.views.Forms.ReviewForm import ReviewForm
import datetime

def review(request, product_id):
    # ログインしているか確認する
    if not "userid" in request.session:
        return redirect("/polls/login")

    # TODO画像を載せる
    if request.method == "GET":
        product = Product().get_one_product(product_id)
        userid = request.session["userid"]
        try:
            review = Review().get_one_review(userid+product_id)
            form = ReviewForm(initial=dict(title=review.title ,comment=review.comment))
            params = {
                "product" : product,
                "title" : review.title,
                "comment" : review.comment,
                "review" : review.reviewStar,
                "form" : form
            }
        except models.Review.DoesNotExist as e:
            params = {
                "product": product,
                "review" : 1,
                "form": ReviewForm
            }

        return render(request, 'polls/review.html', params)
    elif request.method == "POST":
        rv = Review()
        productid = request.POST["productid"]
        title = request.POST["title"]
        comment = request.POST["comment"]
        review = request.POST["review"]
        user_id = request.session['userid']  # useridだけをとる
        product = Product().get_one_product(productid)
        form = ReviewForm(request.POST , initial=dict(title=title , comment=comment))

        if not form.is_valid():
            print("バリデーションエラー:review()")
            print(form.errors)

        params = {
            "review": review,
            "product": product,
            "title": title,
            "comment": comment,
            "form" : form
        }
        check_comment = re.sub("。|、|（|）| " , "" , str(comment))
        if not check_comment.isalnum() and not check_comment.isalpha():
            params["msg"] = "特殊文字を使用しないでください"
            return render(request , "polls/review.html" , params)
        try:
            reviewid = (user_id + productid)
            rv.register_review(reviewid ,user_id , productid , review, title, comment)
        except models.Review.DoesNotExist as e:
            print(e)
            return render(request, 'polls/review.html', params)
        except BaseException as e:
            print(e)
            params["title_msg"] = "文字数上限は50文字です"
            return render(request, 'polls/review.html', params)
        return redirect("/polls/productDetails/" + productid)
