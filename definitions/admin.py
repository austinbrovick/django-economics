from django.contrib import admin

from .models import Definition



class DefinitionModelAdmin(admin.ModelAdmin):
    pass



admin.site.register(Definition, DefinitionModelAdmin)

