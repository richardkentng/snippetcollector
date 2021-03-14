from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Group, Tag, Snippet
from .forms import SnippetForm, GroupForm

# Create your views here.
def snippets(request):
    # query all snippets
    snippets = Snippet.objects.all()
    # query all groups
    groups = Group.objects.all()
    # send empty instance of SnippetForm
    snippet_form = SnippetForm()
    return render(request, 'snippets/index.html', {'snippets': snippets, 'snippet_form': snippet_form, 'groups': groups})

def new_snippet(request):
    # populate snippet form with post data
    snippet_form = SnippetForm(request.POST)
    snippet_form.save()
    return redirect('snippets')

def edit_snippet(request, snippet_id):
    # query snippet by id
    snippet = Snippet.objects.get(id=snippet_id)
    snippet.body = request.POST["body"]
    snippet.save()
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

def groups(request):
    # query groups and send to template
    groups = Group.objects.all()
    # send empty instance of GroupForm to template
    group_form = GroupForm()
    return render(request, 'groups.html', {'groups': groups, 'group_form': group_form})

def new_group(request):
    # populate instance of GroupForm with post data
    group_form = GroupForm(request.POST)
    group_form.save()
    return redirect('groups')

def delete_group(request, group_id):
    # query specific group to delete
    group = Group.objects.get(id=group_id)
    group.delete()
    return redirect('groups')

def assoc_tag_to_group(request, group_id):
    # create tag from request-post data
    tag = Tag(name=request.POST['tag'], group_id=group_id)
    tag.save()
    return redirect('groups')

def unassoc_tag_from_group(request, tag_id):
    # query for specific tag, remove foreign key
    tag = Tag.objects.get(id=tag_id)
    tag.group_id = None
    tag.save()
    return redirect('groups')
