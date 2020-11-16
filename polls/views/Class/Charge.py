from datetime import datetime

from polls import models
from polls.models import PollsCharginghistory, User


class Charge:
    date = ""            # 日付
    amount = 0           # 入金額
    remaining_money = 0  # 残高

    # 履歴の取得
    def get_chargehistory(self, userID):
        all = PollsCharginghistory.objects.filter(userid=userID)
        if all.exists():
            return all
        raise models.PollsChargingHistory.DoesNotExist


