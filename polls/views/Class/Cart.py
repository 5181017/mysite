from polls import models
from polls.views.Class.Product import Product


class Cart:
    product = Product()  # 商品
    quantity = 0         # 個数

    # カートの削除
    def delete_cart(self, userid, productid):
        data = models.Cart.objects.filter(userID=userid, productID=productid)
        data.delete()  # DELETEが実行される

    # カートの追加
    def insert_cart(self, userid, productid, quantity):
        data = models.Cart(userID=userid, productID=productid, quantity=quantity)
        data.save()  # INSERTが実行される

    # カートの更新
    def updata_cart(self, userid, productid, quantity):
        data = models.Cart.objects.get(userID=userid, productID=productid)
        data.quantity = quantity
        data.save()  # ここでUPDATEが実行される
