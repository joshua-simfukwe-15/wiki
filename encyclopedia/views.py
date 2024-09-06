from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

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

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    content = forms.CharField(widget=forms.Textarea, label="content")


def create_page(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            # Checks if the title already exists
            if util.get_entry(title) is not None:
                return render(request, "encyclopedia/create_page.html", {
                    "form": form,
                    "error": "An entry with this title already exists."
                })

            # Saves the new entry
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", kwargs={"title": title}))
    else:
        form = NewPageForm()

    return render(request, "encyclopedia/create_page.html", {
        "form": form
    })


class EditPageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label="content")


def edit_page(request, title):
    entry = util.get_entry(title)

    if entry is None:
        error = True
    else:
        error = False

    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            # Save the updated content
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", kwargs={"title": title}))
    
    # If it's a GET request, show the form with the current content pre-populated
    else:
        form = EditPageForm(initial={"content": entry})

    return render(request, "encyclopedia/edit_page.html", {
        "error": error,
        "form": form,
        "title": title
    })

