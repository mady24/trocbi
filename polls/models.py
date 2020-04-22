from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class SousFamille(models.Model):
    sous_famille = models.CharField(max_length=200)
    dexcription = models.CharField(max_length=1000, null=True)
    image = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.sous_famille
    

class NatureBien(models.Model):
    nature = models.CharField(max_length=200)
    famille = models.ForeignKey(SousFamille, on_delete=models.CASCADE)
    def __str__(self):
        return self.nature
    def __int__(self):
        return self.famille



class PostProp(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    nature = models.ForeignKey(NatureBien, on_delete=models.CASCADE)
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
        return '%d'%(self.id)

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=500, blank=True,null=True)
    tel = models.IntegerField(max_length=20,blank=True,null=True)
    def __str__(self):
        return self.address

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='',blank=True,null=True)
    def __int__(self):
        return self.user.id


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Avatar.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.avatar.save()

# Create your models here.
