
from django.urls import path
from .views import*

urlpatterns = [
    path('', home,name='home'),
    path('articles/', articles_list,name='articles'),
    path('details/<int:id>/', details,name='details'),
    path('propos/', propos,name='propos'),
    path('contact/', contact,name='contact'),
]