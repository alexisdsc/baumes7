from django.contrib import admin
from .models import Recherche


class RechercheAdmin(admin.ModelAdmin):
    list_display = ('nom', 'version_ar', 'version_fra', 'explication', 'populaire')
    search_fields = ['version_ar', 'version_fra']


# Register your models here.
admin.site.register(Recherche, RechercheAdmin)

