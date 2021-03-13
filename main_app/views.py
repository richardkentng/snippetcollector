from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Group, Tag, Snippet
# Create your views here.
def snippets(request):
    # query all snippets
    snippets = Snippet.objects.all()
    return render(request, 'snippets/index.html', {'snippets': snippets})

def unassoc_tag(request, snippet_id, tag_id):
    # find snippet with provided id
    snippet = Snippet.objects.get(id=snippet_id)
    # find tag with provided id
    tag = Tag.objects.get(id=tag_id)
    # unassociate them
    snippet.tags.remove(tag)
    return redirect('snippets')
    return HttpResponse('<p>unassoc_tag view funciton!</p>')