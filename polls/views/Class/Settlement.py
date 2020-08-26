from polls.views.Class.Product import Product


class Settlement:
    product = Product()
    quantity = 0
    data = ""

    # 履歴取得
    def get_history(self):
        all = Polls_payhistory.objects.all()
        return all
    # 残高チェック
    # 購入
    # DB取得
    # DB更新
