from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    x = request.GET["fulltext"]
    y = len(x.split())
    return render(request, 'countword.html', {"fulltext": x, "len": y})


def countchar(request):
    x = request.GET["fulltext"]
    y = len(x)
    return render(request, 'countchar.html', {"fulltext": x, "len": y})


def countfreq(request):
    x = request.GET["fulltext"]
    frequency = {}
    s = x.lower()
    s = s.replace(".", " ")
    s = s.replace(",", " ")
    ls = s.split()

    for word in ls:
        if (word in frequency):
            frequency[word] += 1
        else:
            frequency[word] = 1

    print(frequency)
    return render(request, 'countfreq.html', {"fulltext": x, "freq": frequency})


def about(request):

    return render(request, 'about.html')
