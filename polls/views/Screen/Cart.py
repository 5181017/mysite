from django.shortcuts import render, redirect

from polls import models
from polls.views.Class.Cart import Cart
from polls.views.Class.Product import Product


def cart(request):
    # ログインしているか確認する
    if not "userid" in request.session:
        return redirect("/polls/login")

    try:
        if request.method == "GET":
            if 'userid' in request.session:

                userid = request.session["userid"]
                cartList = Cart().get_cart(userid)
                print(cartList)

                list = []  # 追加
                # この段階で画像、商品名、値段が必要
                for proId in cartList.values("productID"):
                    product = Product()
                    product.productid = proId
                    # product.image = product.get_imageurl(proId)
                    product.image = ""
                    if not product.get_one_product(proId['productID']) is None:
                        product.price = int(product.get_price(proId['productID']))
                        product.name = product.get_one_product(proId['productID']).productName
                        product.quantity =Cart().get_product(userid , proId["productID"]).quantity
                    list.append(product)

                params = {"list": list}  # 追加


            else:
                params = {}
            return render(request, "polls/cart.html", params)

        elif request.method == "POST":
            # 値を取得
            buylist = request.POST.getlist("checkbox")
            userid = request.session["userid"]
            quantity = []
            for productid in buylist:
                quantity.append(request.POST[productid])

            if "delete_btn" in request.POST:
                for i in range(len(buylist)):
                    print(buylist[i])
                    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                    Cart().delete_cart(userid, buylist[i])
                return redirect("/polls/cart")

            elif "pay_btn" in request.POST:
                # カートの更新
                for i in range(len(buylist)):
                    Cart().update_cart(userid, buylist[i], quantity[i])
                cartlist = Cart().get_cart(userid)

                list = []
                for b in buylist:
                    product_obj = Product().get_one_product(b)
                    product = Product()
                    product.productid = product_obj.productID
                    product.name = product_obj.productName
                    product.price = product_obj.price
                    product.quantity = Cart().get_product(userid , product_obj.productID).quantity
                    list.append(product)

                params = {
                    "product": list,
                    "buylist": buylist,
                    "quantity": quantity,
                    "total_money": request.POST["total_money"]
                }
                return render(request, "polls/pay.html", params)
    except models.Cart.DoesNotExist as e:
        print(e)
        return render(request, "polls/exception.html", {"errorMsg": "商品が存在しません。"})
    except Exception as e:
        print(e)
        return render(request, "polls/exception.html", {"errorMsg": "DB接続できませんでした。"})
