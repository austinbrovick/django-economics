from django.contrib import admin

from .models import Word, Definition

class WordModelAdmin(admin.ModelAdmin):
    pass

class DefinitionModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Word, WordModelAdmin)
admin.site.register(Definition, DefinitionModelAdmin)
