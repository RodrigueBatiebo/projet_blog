
from django.urls import path
from .views import*

urlpatterns = [
    path('', home,name='home'),
    path('articles/', articles_list,name='articles'),
]