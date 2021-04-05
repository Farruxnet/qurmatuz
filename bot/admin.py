from django.contrib import admin
from . models import TgUser, UserCart, UserSearch
from django.utils.html import format_html
admin.site.site_header = 'Boshqaruv paneli'
admin.site.site_title = 'Boshqaruv paneli'
admin.site.index_title = "Assalomu alaykum!"
admin.site.site_url = None
class UserCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'avto',  'telefon', 'username', 'date', 'deatline', 'status', )

class TgUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'lan', 'balance')

admin.site.register(TgUser, TgUserAdmin)
admin.site.register(UserCart, UserCartAdmin)
admin.site.register(UserSearch)
