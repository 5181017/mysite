from django.shortcuts import render, redirect

from polls import models
from polls.views.Class.Cart import Cart
from polls.views.Class.Product import Product
from polls.views.Class.Settlement import Settlement


def orderhistory(request):
    # ログインしているか確認する
    if not "userid" in request.session:
        return redirect("/polls/login")

    if request.method == "GET":
        id = request.session["userid"]
        try:
            list = []
            history = Settlement().get_settlement(id)
            cart = Cart().get_cart(id)
            for d in history:
                product = Product().get_one_product(d.productID.productID)
                list.append([d.timeStamp.strftime("%Y年%m月%d日"), product.productName , product.productID])
                cartList = []
                for c in cart:
                    cartList.append(c.productID_id)
                print(list[0][0])
            params = {
                "productlist": list,
                "cart" : cartList
                      }
        except models.PayHistory.DoesNotExist:
            params = {"msg" : "履歴がありません"}
        except Exception as e:
            print(e)
            return redirect("/polls/exeption")
        return render(request, "polls/orderHistory.html", params)

