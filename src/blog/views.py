from django.shortcuts import render
from .models import*

# Create your views here.


def home(request):
    article = Articles.objects.filter(status ="publie").order_by("-created_at")[:6]
    return render(request,'index.html',{"articles":article})

def articles_list(request):
    category = request.GET.get("category")  # récupère ?category=reseaux ou ?category=cuniculture
    query = request.GET.get("q")  # recherche par nom

    articles = Articles.objects.filter(status="publie")

    if category:
        articles = articles.filter(categorie=category)

    if query:
        articles = articles.filter(nom__icontains=query)

    return render(request, "articles.html", {"art": articles})

def details(request,id):
    detail = Articles.objects.filter(id==id)
    return render(request,"details.html",{"detail":detail})