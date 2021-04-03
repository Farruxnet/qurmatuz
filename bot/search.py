import telebot
from telebot import types
from . models import TgUser, UserCart
from . const import LAN, USER_STEP
from django.conf import settings
from botconfig.models import PodCategory, Category, Avto, AvtoKub, Viloyat, Tuman, StartNarx, Paket
from . service import Service

def search(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        pass
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        pass
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        pass
