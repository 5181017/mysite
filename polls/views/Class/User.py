from polls import models
from polls.views.Class.Cart import Cart


class User:
    userId = ""          # ユーザID
    name = ""            # 名前
    remaining_money = 0  # 残高
    address = ""         # 住所
    cart = Cart()        # カート

    # 認証
    def auth(self , userPass):
        user = models.User.objects.filter(userID=self.userId , pw=userPass)
        if(user.exists()):
            return user

        return ValueError

    # ユーザの登録
    def register_user(self , userId , userName , userPass):
        user = models.User.objects.filter(userID=self.userId)
        
    # ユーザの更新
    # ユーザの削除
    # ユーザの取得
    # 残高のチャージ
