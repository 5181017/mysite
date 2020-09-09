from polls import models
from polls.views.Class.Cart import Cart


class User:

    # 認証
    def auth(self, userID, pw):
        user = models.User.objects.filter(userID=userID, pw=pw)
        if user.exists():
            return user

        raise models.User.DoesNotExist

    # ユーザの登録
    def register_user(self, userID, name, pw):
        user = models.User.objects.filter(userID=userID)  # ユーザが存在しない場合DoesNotExist(エラー)を返す。
        if user.exists():
            raise models.User.DoesNotExist
        models.User(
            userID=userID,
            name=name,
            pw=pw,
            money=self.remaining_money,
            address=self.address
        ).save()  # save()が失敗するとTransactionManagementErrorになるかも

    # ユーザの更新
    def update_user(self, userID, name, address):
        models.User.objects.get(userID=userID).update(name=name,address=address)  # ユーザが存在しない場合DoesNotExist(エラー)を返す。

    # ユーザの削除
    def delete_user(self , userID):
        models.User.objects.get(userID=userID).delete()

    # ユーザの取得
    def get_user(self, userID):
        user = models.User.objects.filter(userID=userID)
        if user.exists() and user.count() == 1:
            return user
    #チャージ
    def charge_money(self , userID , money ):
        user = models.User.objects.get(userID=userID)
        if money >= 0:
            money = user.money + money
            user.money = money
            user.save()
