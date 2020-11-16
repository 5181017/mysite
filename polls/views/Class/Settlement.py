from polls import models
from polls.views.Class.Cart import Cart
from polls.views.Class.Product import Product
import datetime

from polls.views.Class.User import User


class Settlement:
    product = Product()  # 商品
    quantity = 0         # 個数
    date = ""            # 日付

    # 履歴取得
    def get_settlement(self, userid):
        data = models.PayHistory.objects.filter(userID=userid)
        if data.exists():
            return data
        raise models.PayHistory.DoesNotExist

    # 残高チェック
    def get_remaining_money(self, userid, total):
        money = models.User.objects.get(userID=userid).money
        if money - int(total) >= 0:
            return True
        return False

    # 購入
    def buy(self, total, userid, products):
        # 残高を減らす
        data = models.User.objects.get(userID=userid)
        data.money = data.money - int(total)
        data.save()  # ここでUPDATEが実行される

        # カートから削除
        for i in range(len(products)):
            paymentID = ("000" + userid + products[i] + str(datetime.datetime.today().strftime("%M%S")))[-10:]
            models.PayHistory(paymentID=paymentID,
                              productID=Product().get_one_product(products[i]),
                              userID=User().get_user(userid),
                              price=Product().get_price(products[i]),
                              quantity=Cart().get_product(userid, products[i]).quantity,
                              total=int(total)
                              ).save()
            Cart().delete_cart(userid, products[i])


