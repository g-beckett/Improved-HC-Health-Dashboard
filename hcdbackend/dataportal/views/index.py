from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


"""
View for our DataPortal's Homepage. Will perform a re-directed to login page if not authenticated.
"""


def index(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('login'))

    context = {}
    return render(request, "dataportal/index.html", context)
