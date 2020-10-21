from polls import models
from polls.views.Class.Product import Product
from polls.views.Class.User import User


class Review:
    product = Product()  # 商品
    # user = User()        # ユーザ
    star = 0             # 星
    title = ""           # タイトル
    comment = ""         # コメント

    # 商品ごとのレビューの取得
    def get_review(self , productid):
        data = models.Review.objects.filter(productID=productid)
        return data

    def get_one_review(self , reviewid):
        data = models.Review.objects.get(reviewID=reviewid)
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
    def register_review(self, reviewid , userid, productid , reviewstar, title, comment):
        user = User().get_user(userid)
        product = Product().get_one_product(productid)
        data = models.Review(reviewID=reviewid , userID=user, productID=product , reviewStar=reviewstar, title=title, comment=comment)
        data.save()  # INSERTが実行される
