from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('snippets/', views.snippets, name="snippets"),
    path('snippets/new', views.new_snippet, name="new_snippet"),
    path('snippets/<int:snippet_id>/delete', views.delete_snippet, name="delete_snippet"),
    path('snippets/<int:snippet_id>/edit', views.edit_snippet, name="edit_snippet"),
    path('snippets/<int:snippet_id>/unassoc_tag/<int:tag_id>/', views.unassoc_tag, name="unassoc_tag"),
    path('snippets/<int:snippet_id>/findOrCreate_assoc_tag/', views.findOrCreate_assoc_tag, name="findOrCreate_assoc_tag"),
    path('groups/', views.groups, name="groups"),
    path('groups/new', views.new_group, name="new_group"),
    path('groups/<int:group_id>/delete/', views.delete_group, name="delete_group"),
    path('groups/<int:group_id>/assoc_tag_to_group/', views.assoc_tag_to_group, name="assoc_tag_to_group"),
    path('groups/<int:tag_id>/unassoc_tag_from_group/', views.unassoc_tag_from_group, name="unassoc_tag_from_group"),
    path('accounts/signup/',views.signup, name="signup"),
]