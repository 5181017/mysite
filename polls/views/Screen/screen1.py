from django.shortcuts import render
from datetime import datetime

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    productName = ""
    if request.POST.get('productName'):
        productName = request.POST.get("productName")

    params = {
        "productName": productName
    }
    return render(request, 'polls/index.html' , params)
