from django.db import models
from django.utils import timezone

ETAT_ACHAT = (
    ("NEUF", "NEUF"),
    ("DEUXIEME MAIN", "DEUXIEME MAIN"),
    ("OCCASION", "OCCASION"),
    ("INCONU", "INCONU")
)

ETAT_ACTUEL = (
    ("NEUF","NEUF"),
    ("BON ETAT","BON ETAT"),
    ("MOYEN","MOYEN"),
    ("MEDIOCRE","MEDIOCRE"),
    ("TRES DEGRADE","TRES DEGRADE")
)

TYPE = (
    ("offre","offre"),
    ("demande","demande")
)


class NatureBien(models.Model):
    nature = models.CharField(max_length=200)
    def __str__(self):
        return self.nature

class SousFamille(models.Model):
    sous_famille = models.CharField(max_length=200)
    dexcription = models.CharField(max_length=1000, null=True)
    def __str__(self):
        return self.sous_famille

class PostProp(models.Model):
    name = models.CharField(max_length=200)
    nature = models.ForeignKey(NatureBien, on_delete=models.CASCADE)
    sous_famille = models.ForeignKey(SousFamille, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    durée_util = models.IntegerField(max_length=10, null=True)
    prix_achat = models.FloatField(max_length=10)
    etat_achat = models.CharField(max_length = 200,choices=ETAT_ACHAT, null=True)
    etat_actuel = models.CharField(max_length = 200,choices=ETAT_ACTUEL, null=True)
    valeur_estime = models.FloatField
    typeProp = models.CharField(max_length = 200, choices=TYPE)
    pub_date = models.DateTimeField(timezone.now())
    image1 = models.ImageField(blank=True, null=True)
    image2 = models.ImageField(blank=True, null=True)
    image3 = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.name

class PostSearch(models.Model):
    name = models.CharField(max_length=200)
    nature = models.ForeignKey(NatureBien, on_delete=models.CASCADE)
    sous_famille = models.ForeignKey(SousFamille, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    durée_util = models.IntegerField(max_length=10)
    etat_actuel = models.CharField(max_length = 200,choices=ETAT_ACTUEL)
    budget = models.FloatField
    pub_date = models.DateTimeField(timezone.now())
    def __str__(self):
        return self.name

# Create your models here.
