from polls import models
from polls.views.Class.Cart import Cart


class User:
    userId = ""          # ユーザIDa
    name = ""            # 名前
    remaining_money = 0  # 残高
    address = ""         # 住所
    cart = Cart()        # カート

    # 認証
    def auth(self , userPass):
        user = models.User.objects.filter(userID=self.userId , pw=userPass)
        if(user.exists()):
            return user

        raise models.User.DoesNotExist

    # ユーザの登録
    def register_user(self, userID, name, pw):
        user = models.User.objects.filter(userID=self.userID)

        if user.exists():
            return "すでに存在します"

        register = models.User(userID=userID, name=name, pw=pw, money=self.remaining_money, address=self)
        models.User.save(register)
        
    # ユーザの更新
    def update_user(self, money, address, cart):
        print("hello")
    # ユーザの削除
    # ユーザの取得
    # 残高のチャージ
