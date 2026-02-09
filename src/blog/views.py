from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from django.core.mail import send_mail
from django.contrib import messages

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
    detail = get_object_or_404(Articles,id=id)
    return render(request,"details.html",{"detail":detail})

def propos(request):
    return render(request,"propos.html")




def contact(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        email_client = request.POST.get('email')
        sujet = request.POST.get('sujet')
        message_contenu = request.POST.get('message')

        # Composition de l'email
        corps_email = f"Nouveau message de {nom} ({email_client}) :\n\n{message_contenu}"
        
        try:
            send_mail(
                sujet,          # Objet du mail
                corps_email,    # Corps du message
                email_client,   # Expéditeur (le client)
                ['rodriguebatiebo5@gmail.com'], # Votre adresse de réception
                fail_silently=False,
            )
            messages.success(request, "Merci ! Votre message a été envoyé.")
        except Exception as e:
            messages.error(request, "Une erreur est survenue lors de l'envoi.")

        return redirect('contact') # Redirige vers la page de contact

    return render(request, 'contact.html')