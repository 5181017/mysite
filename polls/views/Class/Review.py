from polls import models
from polls.views.Class.Product import Product
from polls.views.Class.User import User


class Review:
    product = Product()
    user = User()
    star = 0
    title = ""
    comment = ""

    # レビューの取得
    def get_review(self, productid):
        all = models.Review.object.filter(productID=productid)
        return all

    # レビューの削除
    def get_review(self, reviewid):
        data = models.Review.object.filter(reviewID=reviewid)
        data.delete()  # DELETEが実行される

    # レビューの更新
    def get_review(self, reviewid, reviewstar):
        data = models.Review.object.filter(reviewID=reviewid)
        data.reviewstar = 'new Name'
        data.save()  # ここでUPDATEが実行される

    # レビューの登録
    def get_review(self, userid, reviewstar, title, comment):
        data = models.Review(userID=userid, reviewStar=reviewstar, title=title, comment=comment)
        data.save()  # INSERTが実行される
