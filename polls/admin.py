from django.contrib import admin

from .models import NatureBien
from .models import SousFamille
from .models import PostProp
from .models import PostSearch

admin.site.register(NatureBien)
admin.site.register(SousFamille)
admin.site.register(PostProp)
admin.site.register(PostSearch)

# Register your models here.
