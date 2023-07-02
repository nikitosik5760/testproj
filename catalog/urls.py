from django.urls import path
from .views import *

urlpatterns = [
    path('', CatalogIndexView.as_view(), name='calatog'),
    path('<slug:slug>/', CatalogIndexView.as_view(), name='category')

]
