from django.contrib import admin
from .models import Group, Tag, Snippet
# Register your models here.
admin.site.register(Group)
admin.site.register(Tag)
admin.site.register(Snippet)