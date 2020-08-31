from polls import models
from polls.models import Category


class Category:
    categoryId = ""    # カテゴリーID
    categoryName = ""  # カテゴリー名

    # カテゴリーの取得
    def get_category(self):
        data = models.Category.objects.all()
        return data
