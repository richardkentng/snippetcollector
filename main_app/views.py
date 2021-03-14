from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Group, Tag, Snippet
from .forms import SnippetForm

# Create your views here.
def snippets(request):
    # query all snippets
    snippets = Snippet.objects.all()
    # send empty instance of SnippetForm
    snippet_form = SnippetForm()
    return render(request, 'snippets/index.html', {'snippets': snippets, 'snippet_form': snippet_form})

def new_snippet(request):
    # populate snippet form with post data
    snippet_form = SnippetForm(request.POST)
    snippet_form.save()
    return redirect('snippets')

def delete_snippet(request, snippet_id):
    # find snippet, delete it
    snippet = Snippet.objects.get(id=snippet_id)
    snippet.delete()
    return redirect('snippets')

def unassoc_tag(request, snippet_id, tag_id):
    # find snippet with provided id
    snippet = Snippet.objects.get(id=snippet_id)
    # find tag with provided id
    tag = Tag.objects.get(id=tag_id)
    # unassociate them
    snippet.tags.remove(tag)
    return redirect('snippets')


def findOrCreate_assoc_tag(request, snippet_id):
    # find snippet with provided id
    snippet = Snippet.objects.get(id=snippet_id)
    # find or create tag with provided id
    foundOrCreated_tag = Tag(name=request.POST['tag'])
    foundOrCreated_tag.save()
    # tag = Tag.objects.get(id=tag_id)
    # associate them
    snippet.tags.add(foundOrCreated_tag)
    return redirect('snippets')
