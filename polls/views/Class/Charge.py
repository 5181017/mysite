class Charge:
    date = ""            # 日付
    amount = 0           # 入金額
    remaining_money = 0  # 残高

    # 履歴の取得
    def get_charge(self):
        data = Charge.objects.all()
        return data
