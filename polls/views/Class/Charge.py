from polls import models
from polls.models import PollsCharginghistory


class Charge:
    date = ""            # 日付
    amount = 0           # 入金額
    remaining_money = 0  # 残高

    # 履歴の取得
    def get_chargehistory(self, userid):
        all = PollsCharginghistory.objects.filter(userID=userid)
        if all.exists():
            return all
        raise models.PollsChargingHistory.DoesNotExist

