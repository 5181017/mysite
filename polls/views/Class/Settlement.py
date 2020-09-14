from polls import models
from polls.views.Class.Cart import Cart
from polls.views.Class.Product import Product


class Settlement:
    product = Product()  # 商品
    quantity = 0         # 個数
    date = ""            # 日付

    # 履歴取得
    def get_settlement(self, userid):
        data = models.PayHistory.objects.filter(userID=userid)
        if data.exist():
            return data
        raise models.PayHistory.DoesNotExist

    # 残高チェック
    def get_remaining_money(self, userid, total):
        money = models.User.objects.filter(userID=userid).values("money")
        if money - total >= 0:
            return True
        return False

    # 購入
    def buy(self, total, userid, products):
        # 残高を減らす
        data = models.User.objects.get(userID=userid)
        data.money = data.money - total
        data.save()  # ここでUPDATEが実行される

        # カートから削除
        cart = Cart()
        for i in 1:
            cart.delete_cart(userid, products[i])
