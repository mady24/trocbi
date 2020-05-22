from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.core.paginator import Paginator
from django.core.mail import send_mail

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
    nss = 'none'
    if request.method == 'POST':

        if request.POST['news'] != None:
            ns = NewsLetter(
               mail=request.POST['news']
            )
            try:
                ns.save()
                nss = 'good'
            except:
                nss = 'bad'

    context = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        post = PostProp.objects.filter(name__icontains=url_parameter)
    else:
        post = []
    context["post"] = post
    if request.is_ajax():
        html = render_to_string(
            template_name='polls/template/result.html',
            context={'post':post}
        )

        data_dict = {"html_from_view": html}

    sousFamille = SousFamille.objects.order_by('sous_famille')
    sf = SousFamille.objects.order_by('sous_famille')[0:3]
    sf1 = SousFamille.objects.order_by('sous_famille')[3:6]
    sf2 = SousFamille.objects.order_by('sous_famille')[6:9]
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
    p2 = []
    for n in sf2:
        prop = NatureBien.objects.filter(famille=n)
        #if(len(prop)>0):
        print(prop)
        p2.append(prop)
    
    print(p2)
    template = loader.get_template('polls/template/index.html')
    prop = PostProp.objects.order_by("-pub_date")[:3]
    zip1 = zip(sf,p)
    zip2 = zip(sf1,p1)
    zip3 = zip(sf2,p2)
    context = { 
        'sousFamille': sousFamille,
        'prop': prop, 
        'sf': zip1,
        'sf1': zip2,
        'sf2': zip3,
        'nss': nss
    }
    return HttpResponse(template.render(context, request))

def search(request):
    sousFamille = SousFamille.objects.order_by('sous_famille')
    ctx = {}
    ctx['sousFamille'] = sousFamille
    url_parameter = request.GET.get("q")

    if url_parameter:
        post = PostProp.objects.filter(name__icontains=url_parameter)
    else:
        post = []
    ctx["post"] = post
    if request.is_ajax():
        html = render_to_string(
            template_name='polls/template/result.html',
            context={'post':post}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)
    print(request.POST)
    cat = request.POST['categorie']
    searched = request.POST['searched']
    sf = SousFamille.objects.get(sous_famille__icontains=cat)
    typ = NatureBien.objects.filter(famille=sf)
    prop = []
    #prop = PostProp.objects.filter(name__icontains=searched)
    for t in typ:
        
        pro = PostProp.objects.filter(name__icontains=searched,nature=t)
        print(pro)
        prop.append(pro)
    print(prop)
    ctx['prop'] = prop
    return render(request, 'polls/template/search.html', context=ctx)

def cat(request, cat_id):
    context = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        post = PostProp.objects.filter(name__icontains=url_parameter)
    else:
        post = []
    context["post"] = post
    if request.is_ajax():
        html = render_to_string(
            template_name='polls/template/result.html',
            context={'post':post}
        )

        data_dict = {"html_from_view": html}

    page = request.GET.get('page', 1)
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
    pag = Paginator(prop, 2)
    prop = pag.page(page)
    context = {
        'sousFamille': sousFamille,
        'prop': prop,
        'p': p,
    }
    return HttpResponse(template.render(context, request))

def list(request):
    context = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        post = PostProp.objects.filter(name__icontains=url_parameter)
    else:
        post = []
    context["post"] = post
    if request.is_ajax():
        html = render_to_string(
            template_name='polls/template/result.html',
            context={'post':post}
        )

        data_dict = {"html_from_view": html}

    page = request.GET.get('page', 1)
    sousFamille = SousFamille.objects.order_by('sous_famille')
    template = loader.get_template('polls/template/list.html')
    prop = PostProp.objects.order_by("-pub_date")
    pag = Paginator(prop, 2)
    prop = pag.page(page)
    context = {
        'sousFamille': sousFamille,
        'prop': prop, 
    }
    return HttpResponse(template.render(context, request))

def detail(request, postProp_id):

    if request.method == 'POST':
        first = request.POST['first']
        last = request.POST['last']
        name = request.POST['name']
        iden = request.POST['id']
        valeur = request.POST['valeur']
        prix = request.POST['prix']
        comment = request.POST['comment']
        mail = request.POST['mail']
        send_mail(
            f'Proposition de { first} { last  }',
            f'Bonjour { request.user.first_name } { request.user.last_name} \n { first } { last  } vous a fait une proposition pour votre article {  name} portant la référence { iden } d\'une valeur de { valeur }. \n Sa proposition financiaire est de: { prix }. \n Son message est le suivant: \n { comment }. \n Merci et à très bientôt sur trocbi.sn ',
            'thiape18@gmail.com',
            [f'{ mail }'],
            fail_silently=False,
        )

    context = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        post = PostProp.objects.filter(name__icontains=url_parameter)
    else:
        post = []
    context["post"] = post
    if request.is_ajax():
        html = render_to_string(
            template_name='polls/template/result.html',
            context={'post':post}
        )

        data_dict = {"html_from_view": html}
    try:
        sousFamille = SousFamille.objects.order_by('sous_famille')
        posts = PostProp.objects.get(pk=postProp_id)
        usr = User.objects.get(pk=posts.user_id)
        oth = PostProp.objects.filter(user_id=posts.user_id).exclude(pk=postProp_id).order_by('-pub_date')[:4]
    except PostProp.DoesNotExist:
        raise Http404("Question does not exist")
    context = {'posts': posts,'sousFamille': sousFamille, 'usr': usr, 'oth': oth}
    return render(request, 'polls/template/detail.html',context=context )

def passer(request):
    sousFamille = SousFamille.objects.order_by('sous_famille')
    nature = NatureBien.objects.order_by('nature')
    return render(request, 'polls/template/postPro.html', {'sousFamille': sousFamille, 'etatA': ETAT_ACTUEL, 'etatAC': ETAT_ACHAT, 'nat': nature})

def passerAjouter(request):
    print(request.POST)
    if(request.POST['type'] == 'demande'):
        name = request.POST['nameA']
        nn = request.POST['nat']
        l_des = request.POST['l_des']
        typeA = 'demande'
        du = request.POST['du']
        eac = request.POST['eac']
        prix = request.POST['prix']
        desc = request.POST['desc']

        propIns = PostProp(
            name=name,
            nature=NatureBien.objects.get(pk=nn),
            typeProp=typeA,
            l_descrip=l_des,
            durée_util=du,
            etat_actuel=eac,
            prix_achat=prix,
            description=desc,
            pub_date = timezone.now(),
            user = request.user
        )
        propIns.save()
    if(request.POST['type'] == 'offre'):
        name = request.POST['nameA']
        nn = request.POST['nat']
        typeA = 'offre'
        l_des = request.POST['l_des']
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
            l_descrip=l_des,
            durée_util=du,
            etat_achat=ea,
            etat_actuel=eac,
            prix_achat=prix,
            description=desc,
            pub_date=timezone.now(),
            image1=img1,
            image2=img2,
            image3=img3,
            user = request.user
        )
        propIns.saveDemande()
    return HttpResponseRedirect(reverse('index'))

def loginform(request):
    return render(request, 'registration/login.html')

def loginprocess(request):
    username = request.POST['logID']
    password = request.POST['passwd']
    user = authenticate(request, username=username, password=password)
    try:
        if user is not None:
            print(user)
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    except:
        error = True
        return HttpResponseRedirect(reverse('login', {error}))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def signup(request):
    context = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        post = PostProp.objects.filter(name__icontains=url_parameter)
    else:
        post = []
    context["post"] = post
    if request.is_ajax():
        html = render_to_string(
            template_name='polls/template/result.html',
            context={'post':post}
        )

        data_dict = {"html_from_view": html}
    sousFamille = SousFamille.objects.order_by('sous_famille')
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
    context = {'form': form, 'sousFamille': sousFamille}
    return render(request, 'registration/signup.html', context=context)

@login_required
@transaction.atomic
def profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        avatar_form = AvatarForm(request.POST, request.FILES, instance=request.user.avatar)
        if user_form.is_valid() and profile_form.is_valid() and avatar_form.is_valid():
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
