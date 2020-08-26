# カテゴリのインスタンスを渡す セッション
from django.shortcuts import render

from polls.views.Class.Category import Category


def home(request):
    category = Category().get_category()
    request.session["category"] = category
    params = {"category": category}
    return render(request, "polls/home.html", params)

# 例 def get(request):
#       str = request.session.get("category")
#       return str
