from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .models import PostProp
from .models import SousFamille
from .models import PostSearch
from .models import NatureBien
from .form import *

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
    sf = SousFamille.objects.order_by('sous_famille')[1:5]
    sf1 = SousFamille.objects.order_by('sous_famille')[5:9]
    p = []
    for n in sf:
        prop = NatureBien.objects.filter(famille=n)
        #if(len(prop)>0):
        print(prop)
        p.append(prop)
    
    print(p)
    p1 = []
    for n in sf1:
        prop = NatureBien.objects.filter(famille=n)
        #if(len(prop)>0):
        print(prop)
        p1.append(prop)
    
    print(p1)
    template = loader.get_template('polls/template/index.html')
    prop = PostProp.objects.order_by("-pub_date")
    zip1 = zip(sf,p)
    zip2 = zip(sf1,p1)
    context = {
        'sousFamille': sousFamille,
        'prop': prop, 
        'sf': zip1,
        'sf1': zip2,
    }
    return HttpResponse(template.render(context, request))

def cat(request, cat_id):
    sousFamille = SousFamille.objects.order_by('sous_famille')
    sf = SousFamille.objects.get(pk=cat_id)
    print(sf)
    nature = NatureBien.objects.filter(famille=sf)
    print(nature)
    template = loader.get_template('polls/template/listcat.html')
    p = []
    for n in nature:
        prop = PostProp.objects.filter(nature=n)
        #if(len(prop)>0):
        print(prop)
        p.append(prop)
    
    print(p)
    prop = PostProp.objects.order_by('id')
    context = {
        'sousFamille': sousFamille,
        'prop': prop,
        'p': p,
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
        nn = request.POST['nat']

        typeA = 'demande'
        du = request.POST['du']
        eac = request.POST['eac']
        prix = request.POST['prix']
        desc = request.POST['desc']

        propIns = PostProp(
            name=name,
            nature=NatureBien.objects.get(pk=nn),
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
        nn = request.POST['nat']
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
            nature=NatureBien.objects.get(pk=nn),
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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
@transaction.atomic
def profile(request):
    profile = Avatar.objects.filter(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        avatar_form = AvatarForm(request.FILES['avatar'], instance=request.user.avatar)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            avatar_form.save()
            messages.success(request, 'Votre profile a été mis a jour avec succès')
            return redirect('profile')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        avatar_form = AvatarForm( instance=request.user.avatar)
    return render(request, 'registration/profil.html',{
        'user_form': user_form,
        'profile_form': profile_form,
        'avatar_form': avatar_form,
        'profile': profile
    })

# Create your views here.
