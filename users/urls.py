
from django.urls import path, include
from rest_framework import routers
from users.views import SyndicViewSet, CoproprieteViewSet, LotViewSet, CoproprietaireViewSet, DocumentCoproViewSet, DocumentViewSet

router = routers.DefaultRouter()
router.register(r'syndic', SyndicViewSet, basename='syndic')
router.register(r'copropriete', CoproprieteViewSet, basename='copropriete')
router.register(r'lot', LotViewSet, basename='lot')
router.register(r'coproprietaire', CoproprietaireViewSet, basename='coproprietaire')
router.register(r'documentcopro', DocumentCoproViewSet, basename='documentcopro')
router.register(r'document', DocumentViewSet, basename='document')


urlpatterns = [
    path('', include(router.urls)),
]




