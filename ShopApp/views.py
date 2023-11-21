from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def PageUrl_2(request):
    return render(request, "PageUrl2.html", context={'data': [1, 2]})


def PageUrl_3(request):
    return render(request, "PageUrl3.html")


def PageUrl_4(request):
    return render(request, "PageUrl4.html")


def PageUrl_5(request):
    return render(request, "PageUrl5.html")
