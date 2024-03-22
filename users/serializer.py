
# from rest_framework import serializers
# from .models import Syndic, Copropriete, Lot, Coproprietaire, DocumentCopro, Document

# class SyndicSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Syndic
#         fields = ('id', 'nom', 'prenom', 'mail', 'telephone', 'copropriete_gere')

# class DocumentCoproSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DocumentCopro
#         fields=('id', 'type')

# class CoproprieteSerializer(serializers.ModelSerializer):
#     forkey_id = serializers.PrimaryKeyRelatedField(source='forkey', queryset=Syndic.objects.all())
#     documentcopro_id = serializers.PrimaryKeyRelatedField(source='documentcopro', queryset=DocumentCopro.objects.all())
#     class Meta:
#         model = Copropriete
#         fields = ('id', 'nom', 'adresse', 'autre_info', 'documentcopro_id', 'forkey_id')

# class CoproprietaireSerializer(serializers.ModelSerializer):
#     forkey_id = serializers.PrimaryKeyRelatedField(source='forkey', queryset=Syndic.objects.all())

#     class Meta:
#         model = Coproprietaire
#         fields = ('id', 'nom', 'prenom', 'mail', 'telephone', 'copropriete_gere', 'forkey_id')

# class DocumentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Document
#         fields=('id', 'type')

# class LotSerializer(serializers.ModelSerializer):
#     copropriete_id = serializers.PrimaryKeyRelatedField(source='copropriete', queryset=Copropriete.objects.all())
#     coproprietaire_id = serializers.PrimaryKeyRelatedField(source='coproprietaire', queryset=Coproprietaire.objects.all())
#     document_id = serializers.PrimaryKeyRelatedField(source='document', queryset=Document.objects.all())

#     class Meta:
#         model = Lot
#         fields = ('id', 'copropriete_id', 'coproprietaire_id', 'surface', 'document_id', 'autre')

# class DocumentCoproSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DocumentCopro
#         fields=('id', 'type')






from rest_framework import serializers
from .models import Syndic, Copropriete, Lot, Coproprietaire, DocumentCopro, Document

class SyndicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syndic
        fields = ('id', 'nom', 'prenom', 'mail', 'telephone', 'copropriete_gere')

class DocumentCoproSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCopro
        fields = ('id', 'type')

class CoproprieteSerializer(serializers.ModelSerializer):
    forkey_info = serializers.SerializerMethodField()
    documentcopro_info = serializers.SerializerMethodField()

    class Meta:
        model = Copropriete
        fields = ('id', 'nom', 'adresse', 'autre_info', 'forkey', 'documentcopro', 'forkey_info', 'documentcopro_info')

    def get_forkey_info(self, obj):
        forkey = Syndic.objects.get(id=obj.forkey_id)
        serializer = SyndicSerializer(forkey)
        return serializer.data

    def get_documentcopro_info(self, obj):
        documentcopro = DocumentCopro.objects.get(id=obj.documentcopro_id)
        serializer = DocumentCoproSerializer(documentcopro)
        return serializer.data

class CoproprietaireSerializer(serializers.ModelSerializer):
    forkey_info = serializers.SerializerMethodField()

    class Meta:
        model = Coproprietaire
        fields = ('id', 'nom', 'prenom', 'mail', 'telephone', 'copropriete_gere', 'forkey', 'forkey_info')

    def get_forkey_info(self, obj):
        forkey = Syndic.objects.get(id=obj.forkey_id)
        serializer = SyndicSerializer(forkey)
        return serializer.data

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'type')

class LotSerializer(serializers.ModelSerializer):
    copropriete_info = serializers.SerializerMethodField()
    coproprietaire_info = serializers.SerializerMethodField()
    document_info = serializers.SerializerMethodField()

    class Meta:
        model = Lot
        fields = ('id', 'copropriete', 'coproprietaire', 'surface', 'document', 'autre', 'copropriete_info', 'coproprietaire_info', 'document_info')

    def get_copropriete_info(self, obj):
        copropriete = Copropriete.objects.get(id=obj.copropriete_id)
        serializer = CoproprieteSerializer(copropriete)
        return serializer.data

    def get_coproprietaire_info(self, obj):
        coproprietaire = Coproprietaire.objects.get(id=obj.coproprietaire_id)
        serializer = CoproprietaireSerializer(coproprietaire)
        return serializer.data

    def get_document_info(self, obj):
        document = Document.objects.get(id=obj.document_id)
        serializer = DocumentSerializer(document)
        return serializer.data








