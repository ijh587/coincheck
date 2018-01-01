from django.contrib import admin
from coins.models import Coin

class CoinsAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'offcURL', 'offctwttr')

admin.site.register(Coin, CoinsAdmin)