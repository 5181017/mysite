from django.shortcuts import render

from polls.views.Class.Category import Category


# カテゴリのインスタンスを渡す セッション
def home(request):
    category = Category().get_category()
    # request.session["category"] = category
    params = {"category": category.values("categoryName")}
    # print(category)
    return render(request, "polls/home.html", params)
