# カートに商品を追加


# レビューのインスタンスを渡す
from django.shortcuts import render

from polls.views.Class.Product import Product
from polls.views.Class.Review import Review


def product_details(request , product_id):
        product = Product.get_product(product_id)
        review = Review.get_review(product_id)
        params = {
            "product" : product,
            "review" : review
        }

        return render(request , "polls/product_details" , params)