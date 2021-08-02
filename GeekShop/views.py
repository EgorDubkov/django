from django.shortcuts import render


def index(request):
    context = {
        'slogan': "СУПЕР ПРЕДЛОЖЕНИЕ",
        'title': "Главная"
    }
    return render(request, 'GeekShop/index.html', context)


def contacts(request):
    title = "Контакты"

    context = {
        'title': title,
    }
    return render(request, 'GeekShop/contact.html', context)
