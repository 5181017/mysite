class Charge:
    date = ""            # 日付
    amount = 0           # 入金額
    remaining_money = 0  # 残高

    # 履歴の取得
    def get_charge(self,userID):
        all = ChargingHistory.objects.filter(userID=userID)

        params = {
            'date' : all.timeStamp,
            'amount' : all.addMoney,
            'remaining_money' : sumMoney
        }

        return params
