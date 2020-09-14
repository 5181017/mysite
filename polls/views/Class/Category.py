from polls import models


class Category:
    categoryId = ""    # カテゴリーID
    categoryName = ""  # カテゴリー名

    # カテゴリーの取得
    def get_category(self):
        data = models.Category.objects.all()
        return data
