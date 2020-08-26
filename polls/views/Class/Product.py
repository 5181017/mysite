from polls import models


class Product:
    productId = ""   # 商品ID
    price = 0        # 値段
    image = ""       # 画像
    categoryID = ""  # カテゴリーID

    # 商品の取得
    def get_product(self, productid):
        data = models.product.object.filter(productID=productid)
        return data
