from django.shortcuts import render
import random
# Create your views here.
test_list = [['Первый предмет', 'imtemscr', ''],
                 ['Второй предмет', 'imtemscr', ''],
                 ['Третий предмет', 'imtemscr', ''],
                 ['Четвёртый предмет', 'imtemscr', ''],
                 ['Новый предмет', 'imtemscr', ''],
                 ['Новый предмет', 'imtemscr', ''],
                 ['Новый предмет', 'imtemscr', ''],
                 ['Новый предмет c очень длинным текстом который надо как то настроить', 'imtemscr', ''],
                 ['Предмет не знаю какой уже', 'imtemscr', ''],
                 ['Айтем который давно выбран и есть', 'imtemscr', ''],
                 ['Такой то тут предмет', 'imtemscr', ''],
                 ['Просто новый предмет для тебя', 'imtemscr', ''],
                 ['Оно тебе не надо', 'imtemscr', ''],
                 ['Остаточный предмет', 'imtemscr', ''],
                 ['Новый текст для предмета c очень длинным текстом', 'imtemscr', '']]


def index(request):

    shuffle_list = test_list[:]
    random.shuffle(shuffle_list)

    return render(request, "index.html", context= {'data': shuffle_list })


def PageUrl_2(request):
    return render(request, "PageUrl2.html", context={'data': test_list})


def PageUrl_3(request):
    return render(request, "PageUrl3.html")


def PageUrl_4(request):
    return render(request, "PageUrl4.html")


def PageUrl_5(request):
    return render(request, "PageUrl5.html")
