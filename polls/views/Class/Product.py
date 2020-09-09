from polls import models


class Product:
    productId = ""  # 商品ID
    price = 0  # 値段
    image = ""  # 画像
    categoryID = ""  # カテゴリーID

    # 指定されたカテゴリーIDの商品を取得
    def get_product(self, categoryid):
        data = models.Products.object.filter(categoryid=categoryid)
        return data

    def get_one_product(self, productid):
        data = models.Products.objects.get(productID=productid)
        return data
