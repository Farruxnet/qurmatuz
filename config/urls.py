from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from bot.views import web_hook
from botconfig.views import messages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/', csrf_exempt(web_hook)),
    path('sendmessage/', messages),
]
