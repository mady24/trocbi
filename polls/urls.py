from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('<int:postProp_id>/', views.detail, name='detail'),
    path('passerannonce', views.passer, name='passer'),
    path('passannonceinsertion', views.passerAjouter, name='passerannonceinsertion'),
    path('login', views.loginform, name='login'),
    path('loginprocess', views.loginprocess, name='loginprocess'),
    path('logout', views.logout_view, name="logout"),
    path('signup', views.signup, name="signup"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/resetPwd.html'), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/resetPwdConfirm.html'), name='password_reset_confirm'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='registration/resetPwdDone.html'), name='password_reset_done'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/resetPwdComplete.html'), name='password_reset_complete'),
    path('list/', views.list, name='list'),
    path('profile', views.profile, name='profile'),
    path('cat/<int:cat_id>/', views.cat, name='cat'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
