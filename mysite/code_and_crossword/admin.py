from django.contrib import admin

# Register your models here.

from .models import Code, Crossword

admin.site.register(Code)
admin.site.register(Crossword)