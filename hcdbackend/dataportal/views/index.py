from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "dataportal/index.html", context)
