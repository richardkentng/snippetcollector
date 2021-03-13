from django.shortcuts import render, redirect
from .models import Group, Tag, Snippet
# Create your views here.
def snippets(request):
    # query all snippets
    snippets = Snippet.objects.all()
    return render(request, 'snippets/index.html', {'snippets': snippets})