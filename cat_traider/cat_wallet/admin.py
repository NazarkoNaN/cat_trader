from django.contrib import admin
from cat_wallet.models import *

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    pass
