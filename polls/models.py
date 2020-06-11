from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

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
    l_descrip = models.CharField(max_length=80)
    description = models.CharField(max_length=1000)
    durée_util = models.IntegerField(max_length=10, null=True)
    prix_achat = models.FloatField(max_length=10)
    etat_achat = models.CharField(max_length = 200,choices=ETAT_ACHAT, null=True)
    etat_actuel = models.CharField(max_length = 200,choices=ETAT_ACTUEL, null=True)
    valeur_estime = models.FloatField
    typeProp = models.CharField(max_length = 200, choices=TYPE)
    pub_date = models.DateTimeField(timezone.now())
    image1 = models.ImageField(blank=True, null=True)
    image2 = models.ImageField(blank=True, null=True, default='not-found.png')
    image3 = models.ImageField(blank=True, null=True, default='not-found.png')
    image4 = models.ImageField(blank=True, null=True, default='not-found.png')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    validated = models.BooleanField(default=False)
    def __str__(self):
        return '%d'%(self.id)

    def saveDemande(self):
        super().save()
        if self.image1.path != '':
            img = Image.open(self.image1.path)

            if img.height < 1500 or img.width < 1500:
                output_size = (1500,1500)
                img.thumbnail(output_size)
                img.save(self.image1.path, dpi=(150,150))
        
        if self.image2.path != '':
            img = Image.open(self.image2.path)

            if img.height < 1500 or img.width < 1500:
                output_size = (1500,1500)
                img.thumbnail(output_size)
                img.save(self.image2.path, dpi=(150,150))

        if self.image3.path != '':
            img = Image.open(self.image3.path)

            if img.height < 1500 or img.width < 1500:
                output_size = (1500,1500)
                img.thumbnail(output_size)
                img.save(self.image3.path, dpi=(150,150))
        
        if self.image4.path != '':
            img = Image.open(self.image4.path)

            if img.height < 1500 or img.width < 1500:
                output_size = (1500,1500)
                img.thumbnail(output_size)
                img.save(self.image4.path, dpi=(150,150))

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
    avatar = models.ImageField(default='user.png', upload_to='media',blank=True,null=True)
    def __str__(self):
        return f'{self.user.username} avatar'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.avatar.path, dpi=(150,150))


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Avatar.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.avatar.save()

class NewsLetter(models.Model):
    mail = models.EmailField(max_length=100, blank=False, null=False)
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.mail

# Create your models here.
