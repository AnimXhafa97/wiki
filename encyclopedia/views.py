from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from builtins import any
from . import util

import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_page(request, title):
    page = util.get_entry(title)

    context = {
        'title': title,
        'content': page,
    }

    if page is None:
        return render(request, "encyclopedia/error.html", {'title':title})

    return render(request, "encyclopedia/title.html", context)



def edit(request):
    pass

def save(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    util.save_entry(title, content)
    return HttpResponseRedirect(reverse('index'))


def new_page(request):
    return render(request, "encyclopedia/new.html")

def search(request):
    if request.method == "GET":
        query = request.GET.get('q')
        pages = [x.lower() for x in util.list_entries()]
        results = [s for s in pages if query in s]
        return render(request, "encyclopedia/results.html", {'results':results})

def random(request):
    pass
