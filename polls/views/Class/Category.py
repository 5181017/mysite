from polls.models import Category


class Category:
    categoryId = ""  # カテゴリーID
    categoryName = ""  # カテゴリー名

    # カテゴリーの取得
    def get_category(self):
        all = Category.objects.all()  # 全件取得
        return all
