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
        user = models.User.objects.get(userID=userID)
        user = user.filter(pw=pw)
        if user.exists():
            return user
        else:
            errmsg = "パスワードが違います。"
            return errmsg


    # ユーザの登録
    def register_user(self, userID, name, pw):
        models.User.objects.get(userID=userID)  # ユーザが存在しない場合DoesNotExist(エラー)を返す。
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
