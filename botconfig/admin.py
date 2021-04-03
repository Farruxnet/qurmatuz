from django.contrib import admin
from . models import Config, Avto, AvtoKub, Tuman, Viloyat, Category, PodCategory, StartNarx, Paket, Messages

class ConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        if len(Config.objects.all()) == 3:
            return False
        else:
            return True
    list_display = ('text', 'about')

admin.site.register(Config, ConfigAdmin)
admin.site.register(AvtoKub)
admin.site.register(Avto)
admin.site.register(Viloyat)
admin.site.register(Tuman)
admin.site.register(Category)
admin.site.register(PodCategory)
admin.site.register(StartNarx)
admin.site.register(Paket)
admin.site.register(Messages)
