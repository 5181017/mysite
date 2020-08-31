from polls import models
from polls.views.Class.Product import Product
from polls.views.Class.User import User


class Review:
    product = Product()  # 商品
    user = User()        # ユーザ
    star = 0             # 星
    title = ""           # タイトル
    comment = ""         # コメント

    # レビューの取得
    def get_review(self, productid):
        data = models.Review.object.filter(productID=productid)
        return data

    # レビューの削除
    def delete_review(self, reviewid):
        data = models.Review.object.filter(reviewID=reviewid)
        data.delete()  # DELETEが実行される

    # レビューの更新
    def update_review(self, reviewid, reviewstar):
        data = models.Review.object.filter(reviewID=reviewid)
        data.reviewStar = reviewstar
        data.save()  # ここでUPDATEが実行される

    # レビューの登録
    def register_review(self, userid, reviewstar, title, comment):
        data = models.Review(userID=userid, reviewStar=reviewstar, title=title, comment=comment)
        data.save()  # INSERTが実行される
