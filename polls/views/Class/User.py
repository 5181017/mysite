from polls import models
from polls.views.Class.Cart import Cart


class User:
    userID = ""  # ユーザID
    name = ""  # 名前
    remaining_money = 0  # 残高
    address = ""  # 住所
    cart = Cart()  # カート

    # 認証
    def auth(self, userID, pw):
        user = models.User.objects.filter(userID=userID, pw=pw)
        if user.exists():
            self.userID = user.userID
            self.name = user.name
            self.remaining_money = user.money
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
    def update_user(self, name, address):
        models.User.objects.get(userID=self.userID).update(name=name,
                                                           address=address)  # ユーザが存在しない場合DoesNotExist(エラー)を返す。

    # ユーザの削除
    def delete_user(self):
        models.User.objects.get(userID=self.userID).delete()

    # ユーザの取得
    def get_user(self, userID):
        user = models.User.objects.filter(userID=userID)
        if user.exists() and user.count() == 1:
            return user
