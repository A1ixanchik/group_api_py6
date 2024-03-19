from django.contrib import admin
from .models import Musician, Song, Awards


admin.site.register(Musician)
admin.site.register(Song)
admin.site.register(Awards)

