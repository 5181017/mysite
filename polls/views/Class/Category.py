class Category:
    categoryId = ""    # カテゴリーID
    categoryName = ""  # カテゴリー名

    def get_category(self):
        all = Category.objects.all()
        return all

    # カテゴリーの取得
