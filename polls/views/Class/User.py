import datetime

from polls import models
# from polls.views.Class.Cart import Cart


class User:
    userid = ""     # ユーザーID
    name = ""       # 名前
    money = 0       # 残高
    address = ""    # 住所
    # cart = Cart()   # カート

    # 認証
    def auth(self, userID, pw):
        user = models.User.objects.filter(userID=userID)
        user = user.get(pw=pw)
        return user

    # ユーザの登録
    def register_user(self, userID, name, pw):

        user = models.User.objects.filter(userID=userID)
        if user.exists():
            raise models.User.DoesNotExist
        models.User(
            userID=userID,
            name=name,
            pw=pw,
            money=0,
            address=""
        ).save()  # save()が失敗するとTransactionManagementErrorになるかも

    # ユーザの更新
    def update_user(self, userID, name, address):
        user = models.User.objects.get(userID=userID) # ユーザが存在しない場合DoesNotExist(エラー)を返す。
        user.name = name
        user.address = address
        user.save()


    # ユーザの削除
    def delete_user(self, userID):
        models.User.objects.get(userID=userID).delete()

    # ユーザの取得
    def get_user(self, userID):
        user = models.User.objects.get(userID=userID)
        # if user.exists() and user.count() == 1:
        return user

    # チャージ
    def charge_money(self, userID, money):
        user = models.User.objects.get(userID=userID)
        add_money = money
        if money >= 0:
            money = user.money + money
            user.money = money
            user.save()

        # チャージ履歴の更新

        models.PollsCharginghistory(
            userid=userID,
            addmoney=add_money,
            summoney=money
        ).save()


