from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category
# Create your views here.


class CatalogIndexView(ListView):
    template_name = 'catalog/index.html'
    model = Category

    def get_queryset(self) -> QuerySet[Any]:
        return Category.objects.filter(parent=None)
