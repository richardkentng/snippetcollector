from django.urls import path
from . import views

urlpatterns = [
    path('snippets/', views.snippets, name="snippets"),
    path('snippets/<int:snippet_id>/unassoc_tag/<int:tag_id>/', views.unassoc_tag, name="unassoc_tag"),
]