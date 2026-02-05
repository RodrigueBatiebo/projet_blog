from django.contrib import admin
from .models import Profil, Articles

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ("user", "avatar")  # bio n'existe pas dans ton modèle
    search_fields = ("user__username", "user__first_name", "user__last_name", "user__email")
    list_filter = ("user__is_staff", "user__is_superuser")


@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("nom", "auteur", "status", "created_at", "date_publication")
    search_fields = ("nom", "contenu", "auteur__user__username")
    list_filter = ("status", "created_at", "date_publication")
    ordering = ("-created_at",)
