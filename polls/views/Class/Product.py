from polls import models
from polls.models import Products


class Product:
    productid = ""   # 商品ID
    price = 0        # 値段
    image = ""       # 画像
    categoryid = ""  # カテゴリーID

    # 指定されたカテゴリーIDの商品を取得
    def get_product(self, categoryid):
        data = models.Products.object.filter(categoryid=categoryid)
        return data

    # 特定の商品を取得
    def get_one_product(self, productid):
        data = models.Products.objects.get(productID=productid)
        return data

    # 特定の商品の値段を取得
    def get_price(self, productid):
        data = models.Products.objects.get(productID=productid)
        return data.price

    # 特定の商品の画像URLを取得
    def get_imageurl(self, productid):
        data = models.Products.objects.get(productID=productid)
        return data.imageURL
