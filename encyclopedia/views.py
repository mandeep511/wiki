from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import Markdown
import random
import re

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    title_data = util.get_entry(title)
    if not title_data:
        return render(request, "encyclopedia/appology.html", {
            "error": "Wiki title does not exit"
        })
    markdowner = Markdown()
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "content": markdowner.convert(title_data),
    })

def search(request):
    q = request.GET['q']
    # print(q)
    title_list = util.list_entries()
    # print(title_list)
    found_list = []

    for title in title_list:
        # print(title)
        if re.match(f"{q.strip()}", title.lower()):
            # print("i'm in")
            found_list.append(title)
    # print(found_list)
    return render(request, "encyclopedia/index.html", {
        "entries": found_list
    })

def create(request):
    return render(request, "encyclopedia/create.html")

def random_page(request):
    
    title = random.choice(util.list_entries())
    title_data = util.get_entry(title)
    
    markdowner = Markdown()
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "content": markdowner.convert(title_data)
    })