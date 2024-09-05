from django.shortcuts import render, redirect

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

def search(request):
    query = request.GET.get('q')  # Get the search query from the request
    if query:
        entries = util.list_entries()
        matching_entries = [entry for entry in entries if query.lower() in entry.lower()]

        if len(matching_entries) == 1 and matching_entries[0].lower() == query.lower():
            # If there's an exact match, redirect to that entry's page
            return redirect('entry', title=matching_entries[0])

        # Otherwise, show the search results
        return render(request, "encyclopedia/search.html", {
            "entries": matching_entries,
            "query": query
        })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
