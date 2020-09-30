import uuid

from django.db import models


class Category(models.Model):
    categoryID = models.CharField(primary_key=True, max_length=10)
    categoryName = models.CharField(max_length=50)

    # def __str__(self):
    #   return '<Category:categoryid=' + str(self.categoryid) + ',' +self.categoryName


class User(models.Model):
    userID = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)
    money = models.IntegerField(default=0)
    address = models.CharField(max_length=2048)


class Products(models.Model):
    productID = models.CharField(primary_key=True, max_length=15)
    productName = models.CharField(max_length=255)
    price = models.IntegerField()
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    imageURL = models.CharField(max_length=2048)


class Cart(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    productID = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['userID', 'productID'], name='unique_booking')
        ]


class PayHistory(models.Model):
    paymentID = models.CharField(primary_key=True, max_length=10)
    productID = models.ForeignKey(Products, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    total = models.IntegerField()
    timeStamp = models.DateTimeField(auto_now=True)


class ChargingHistory(models.Model):
    chargeID = models.CharField(primary_key=True, max_length=10)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now=True)
    addMoney = models.IntegerField()
    sumMoney = models.IntegerField()


class Review(models.Model):
    reviewID = models.CharField(primary_key=True, max_length=10)
    productID = models.ForeignKey(Products, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewStar = models.IntegerField()
    title = models.CharField(max_length=50, null=True)
    comment = models.TextField()
