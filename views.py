from django.shortcuts import render


def index(request):
    a = 'Spartak', 'Dynamo', 'Lokomotiv'
    return render(request, 'index.html', context={'name': a})

