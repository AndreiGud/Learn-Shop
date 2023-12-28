from django.shortcuts import render
import random
from django.views import generic
from .models import type_every, types_item, item_catalog
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


class indexListView(generic.ListView):
   #model = item_catalog
    context_object_name = 'data'
    template_name = 'Index.html'
    queryset = item_catalog.objects.order_by('?')


def Catalog(request):
    return render(request, "Catalog.html", context={'data': test_list})


class CatalogListView(generic.ListView):
    model = item_catalog
    context_object_name = 'data'
    template_name = 'Catalog.html'


class CatalogListViewN(generic.DetailView):
    model = item_catalog
    context_object_name = 'my_book_list'
    template_name = 'CatalogItem.html'


def PageUrl_3(request):
    return render(request, "PageUrl3.html")


def PageUrl_4(request):
    return render(request, "PageUrl4.html")


def PageUrl_5(request):
    return render(request, "PageUrl5.html")


def Login(request):
    return render(request, "Login.html")


def Account_User(request):
    return render(request, "UserRoom.html")
