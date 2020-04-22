from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:postProp_id>/', views.detail, name='detail'),
    path('passerannonce', views.passer, name='passer'),
    path('passannonceinsertion', views.passerAjouter, name='passerannonceinsertion'),
    path('login', views.loginform, name='login'),
    path('loginprocess', views.loginprocess, name='loginprocess'),
    path('logout', views.logout_view, name="logout"),
    path('signup', views.signup, name="signup"),
    path('list', views.list, name='list'),
    path('profile', views.profile, name='profile'),
    path('cat/<int:cat_id>/', views.cat, name='cat'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
