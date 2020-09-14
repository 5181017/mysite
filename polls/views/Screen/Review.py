from django.shortcuts import render, redirect

from polls.views.Class.Product import Product
from polls.views.Class.Review import Review


def review(request , product_id):
    #TODO
    # 画像を載せる
    if request.method == "GET":
        # product_id = request.GET.get("product_id")
        product = Product().get_product(product_id)

        params = {
            "product_name" : product.productName,
            "product_img" : product.imageURL,
        }
        return render(request , 'polls/review.html' , params)
    elif request.method == "POST":
        rv = Review()
        reviewstar = request.POST["reviewstar"]
        title = request.POST["title"]
        comment = request.POST["commnet"]
        user_id = request.session['user']        #useridだけをとる
        rv.register_review(user_id , reviewstar , title , comment)
        return redirect("/product/" + product_id)
