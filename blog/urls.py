from django.urls import path

from .views import *
urlpatterns = [
    path('search/', search, name='search'),
    path('random/', random_article, name='random_article'),
    path('<str:slug>/', details, name='details'),
    path('', articles_list, name='blog'),
    path('tag/<str:tag>/', article_tag_list, name='articles_tag_list'),

]
