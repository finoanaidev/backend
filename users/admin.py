from django.contrib import admin

from users.models import Syndic, Copropriete,Lot, Coproprietaire, DocumentCopro,Document

# Register your models here.

admin.site.register(Syndic)
admin.site.register(Copropriete)
admin.site.register(Lot)
admin.site.register(Coproprietaire)
admin.site.register(DocumentCopro)
admin.site.register(Document)
