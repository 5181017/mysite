from polls.views.Class.Cart import Cart


class User:
    userId = ""          # ユーザIDa
    name = ""            # 名前
    remaining_money = 0  # 残高
    address = ""         # 住所
    cart = Cart()        # カート

    # 認証
    # ユーザの登録
    # ユーザの更新
    # ユーザの削除
    # ユーザの取得
    # 残高のチャージ
