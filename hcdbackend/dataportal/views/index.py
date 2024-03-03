from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


def index(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('login'))

    context = {}
    return render(request, "dataportal/index.html", context)
