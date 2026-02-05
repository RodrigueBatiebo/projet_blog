from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profil")
    avatar = models.ImageField(upload_to="image/",blank=True,null=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()}"
    class Meta: 
        verbose_name = "Profil" 
        verbose_name_plural = "Profils" 
        ordering = ["user__last_name", "user__first_name"]

class Articles(models.Model):
    photo = models.ImageField(upload_to="image/",blank=True,null=True)
    auteur = models.ForeignKey(Profil,on_delete=models.CASCADE,related_name="articles")
    nom = models.CharField(max_length=100)
    description = models.TextField()
    contenu = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    choix_status = [
    ("publie", "Publié"),
    ("attente", "attente"),
]

    status = models.CharField(max_length=10,choices=choix_status,default="attente")
    date_publication = models.DateTimeField(blank=True,null=True)

    choix_categorie = [ ("reseaux", "Réseaux informatique"), ("cuniculture", "Cuniculture"), ] 
    categorie = models.CharField(max_length=20, choices=choix_categorie, default="reseaux") 
    
    def save(self, *arguments, **options):
        if self.status == "Publié" and self.published_at is None:
            from django.utils import timezone
            self.date_publication = timezone.now()
        super().save(*arguments, **options)
    def __str__(self):
        return f"{self.nom} - {self.auteur.user.username}"

    class Meta: 
        verbose_name = "Article" 
        verbose_name_plural = "Articles" 
        ordering = ["-created_at"]