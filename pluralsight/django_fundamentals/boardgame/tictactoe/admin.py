from django.contrib import admin

from .models import Game, Move


admin.site.register(Game)  #Register with admin interface so they will show up in the user interface
admin.site.register(Move)