from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout

from .models import PostProp
from .models import SousFamille
from .models import PostSearch
from .models import NatureBien

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

def index(request):
    sousFamille = SousFamille.objects.order_by('sous_famille')
    template = loader.get_template('polls/template/index.html')
    prop = PostProp.objects.order_by("-pub_date")
    context = {
        'sousFamille': sousFamille,
        'prop': prop, 
    }
    return HttpResponse(template.render(context, request))

def list(request):
    sousFamille = SousFamille.objects.order_by('sous_famille')
    template = loader.get_template('polls/template/list.html')
    prop = PostProp.objects.order_by("-pub_date")
    context = {
        'sousFamille': sousFamille,
        'prop': prop, 
    }
    return HttpResponse(template.render(context, request))

def detail(request, postProp_id):
    try:
        sousFamille = SousFamille.objects.order_by('sous_famille')
        post = PostProp.objects.get(pk=postProp_id)
    except PostProp.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/template/detail.html', {'post': post,'sousFamille': sousFamille})

def passer(request):
    sousFamille = SousFamille.objects.order_by('sous_famille')
    nature = NatureBien.objects.order_by('nature')
    return render(request, 'polls/template/postPro.html', {'sousFamille': sousFamille, 'etatA': ETAT_ACTUEL, 'etatAC': ETAT_ACHAT, 'nat': nature})

def passerAjouter(request):
    print(request.POST)
    if(request.POST['type'] == 'demande'):
        name = request.POST['nameA']
        nat = request.POST['nat']
        fam = request.POST['catA']
        typeA = 'demande'
        du = request.POST['du']
        eac = request.POST['eac']
        prix = request.POST['prix']
        desc = request.POST['desc']

        propIns = PostProp(
            name=name,
            nature=NatureBien.objects.get(pk=nat),
            sous_famille=SousFamille.objects.get(pk=fam),
            typeProp=typeA,
            durée_util=du,
            etat_actuel=eac,
            prix_achat=prix,
            description=desc,
            pub_date = timezone.now()
        )
        propIns.save()
    if(request.POST['type'] == 'offre'):
        name = request.POST['nameA']
        nat = request.POST['nat']
        fam = request.POST['catA']
        typeA = 'offre'
        du = request.POST['du']
        eac = request.POST['eac']
        prix = request.POST['prix']
        desc = request.POST['desc']
        da = request.POST['da']
        ea = request.POST['ea']
        img1 = request.FILES['img1']
        img2 = request.FILES['img2']
        img3 = request.FILES['img3']

        propIns = PostProp(
            name=name,
            nature=NatureBien.objects.get(pk=nat),
            sous_famille=SousFamille.objects.get(pk=fam),
            typeProp=typeA,
            durée_util=du,
            etat_achat=ea,
            etat_actuel=eac,
            prix_achat=prix,
            description=desc,
            pub_date=timezone.now(),
            image1=img1,
            image2=img2,
            image3=img3
        )
        propIns.save()
    return HttpResponseRedirect(reverse('index'))

def loginform(request):
    return render(request, 'registration/login.html')

def loginprocess(request):
    username = request.POST['logID']
    password = request.POST['passwd']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        print(user)
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('login'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# Create your views here.
