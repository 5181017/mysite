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
            params = {
                "product": product,
                "review": review,
                "cart" : ""
            }
            if "userid" in request.session:
                userid =request.session["userid"]
                params.update({"cart" : Cart().get_cart(userid)})

            return render(request, "polls/productDetails.html", params)
        except models.User.DoesNotExist as e:
            print(e)
            return redirect("/polls/exception")
        except Exception as e:
            print(e)
            return redirect("/polls/exception")



    if request.method == "POST":
        userid = request.session["userid"]
        productid = request.POST["productid"]
        Cart().insert_cart(userid , productid , 1)
        return redirect("/polls/productDetails/" + productid)

