from django.shortcuts import render

from . import util

from markdown2 import Markdown



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    markdowner = Markdown()

    if entry == None:
        entry = f"## {title.capitalize()}\'s page has not been found"
    entry=markdowner.convert(entry)    
    return render(request, "encyclopedia/entry.html", {
        "title":title,
        "entry": entry
    })

