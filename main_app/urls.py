from django.urls import path
from . import views

urlpatterns = [
    path('snippets/', views.snippets, name="snippets"),
]