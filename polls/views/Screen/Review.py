# レビュー情報登録
from django.shortcuts import render

from polls.views.Class.Product import Product
from polls.views.Class.Review import Review


def review(request , product_id):
    #画像を載せる
    if request.method == "GET":
        product_id = request.GET.get("product_id")
        product = Product().get_product(product_id)
        #画像処理
        product_img = product.get('image')
        params = {

        }
        return render(request , 'polls/review.html')
    elif request.method == "POST":
        rv = Review()
        reviewstar = request.POST["reviewstar"]
        title = request.POST["title"]
        comment = request.POST["commnet"]
        userid = request.session['user']        #useridだけをとる
        rv.register_review(userid , reviewstar , title , comment)
