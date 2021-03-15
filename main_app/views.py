from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Group, Tag, Snippet
from .forms import SnippetForm, GroupForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def snippets(request):
    # query all snippets
    snippets = Snippet.objects.filter(user=request.user)
    # query all groups
    groups = Group.objects.all()
    # send empty instance of SnippetForm
    snippet_form = SnippetForm()
    return render(request, 'snippets/index.html', {'snippets': snippets, 'snippet_form': snippet_form, 'groups': groups})

@login_required
def new_snippet(request):
    # populate snippet form with post data
    snippet_form = SnippetForm(request.POST)
    new_snippet = snippet_form.save(commit=False)
    new_snippet.user = request.user
    try:
        new_snippet.save()
    except:
        print('A snippet with that value already exists!')
    return redirect('snippets')

@login_required
def edit_snippet(request, snippet_id):
    # query snippet by id
    snippet = Snippet.objects.get(id=snippet_id)
    snippet.body = request.POST["body"]
    snippet.save()
    return redirect('snippets')

@login_required
def delete_snippet(request, snippet_id):
    # find snippet, delete it
    snippet = Snippet.objects.get(id=snippet_id)
    snippet.delete()
    return redirect('snippets')

@login_required
def findOrCreate_assoc_tag(request, snippet_id):
    # find snippet with provided id
    snippet = Snippet.objects.get(id=snippet_id)
    # find or create tag with provided id
    tag = Tag(name=request.POST['tag'])
    tag.save()
    # tag = Tag.objects.get(id=tag_id)
    # associate them
    snippet.tags.add(tag)
    return redirect('snippets')
    
@login_required
def unassoc_tag(request, snippet_id, tag_id):
    # find snippet with provided id
    snippet = Snippet.objects.get(id=snippet_id)
    # find tag with provided id
    tag = Tag.objects.get(id=tag_id)
    # unassociate them
    snippet.tags.remove(tag)
    return redirect('snippets')


@login_required
def groups(request):
    # query groups and send to template
    groups = Group.objects.filter(user=request.user)
    # send empty instance of GroupForm to template
    group_form = GroupForm()
    return render(request, 'groups.html', {'groups': groups, 'group_form': group_form})

@login_required
def new_group(request):
    # populate instance of GroupForm with post data
    group_form = GroupForm(request.POST)
    new_group = group_form.save(commit=False)
    new_group.user = request.user
    new_group.save()
    return redirect('groups')

@login_required
def delete_group(request, group_id):
    # query specific group to delete
    group = Group.objects.get(id=group_id)
    group.delete()
    return redirect('groups')

@login_required
def assoc_tag_to_group(request, group_id):
    # create tag from request-post data
    tag = Tag(name=request.POST['tag'], group_id=group_id)
    tag.save()
    return redirect('groups')

@login_required
def unassoc_tag_from_group(request, tag_id):
    # query for specific tag, remove foreign key
    tag = Tag.objects.get(id=tag_id)
    tag.group_id = None
    tag.save()
    return redirect('groups')

def signup(request):
    err_msg = ''
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        # return HttpResponse('<p>post</p>')
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('snippets')
        else:
            err_msg = 'Invalid signup.  Please try again.'
    return render(request, 'registration/signup.html', {'form': form, 'err_msg': err_msg})
        # return HttpResponse('<p>get</p>')