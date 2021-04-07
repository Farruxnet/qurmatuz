from django.shortcuts import render
from django.conf import settings
import telebot
from math import ceil
from telebot import types
from . models import TgUser
from . service import *
from botconfig.models import Category, Config
from . const import LAN, USER_STEP
from django.http.response import HttpResponse
from . search import *
bot = telebot.TeleBot(settings.BOT_TOKEN)
import logging
logging.basicConfig(filename="adas.log", format=' %(asctime)s - %(levelname)s - %(message)s')
logging.info('Session Start')

def web_hook(request):
    if request.method == "POST":
        bot.process_new_updates([telebot.types.Update.de_json(request.body.decode('utf-8'))])
        # bot.set_webhook(url=settings.WEB_HOOK_URL+'/bot/')
        return HttpResponse(status=200)
    s = '<a href="https://api.telegram.org/bot{0}/setWebhook?url={1}/bot/">WEB</a>'.format(settings.BOT_TOKEN, settings.WEB_HOOK_URL)
    return HttpResponse(s)

def home_page(request):
    return HttpResponse("404 page not found")


@bot.message_handler(commands=['start'])
def start_handler(message):
    if TgUser.objects.filter(tg_id=message.chat.id).exists():
        TgUser.objects.filter(tg_id=message.chat.id).update(step=USER_STEP['DEFAULT'])
        for i in Config.objects.filter(lan=Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))):
            bot.send_message(message.chat.id, i.text, reply_markup=home_func(message))
    else:
        save_lan = TgUser(tg_id=message.chat.id, name=message.chat.first_name, step=USER_STEP['LAN'], lan='ru')
        save_lan.save()
        lan_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        button = lan_button.add((types.KeyboardButton(text='🇺🇿 O\'zbek')), (types.KeyboardButton(text='🇺🇿 Узбек')), (types.KeyboardButton(text='🇷🇺 Руский')))
        bot.send_message(message.chat.id, "Tilni tanlang", reply_markup=lan_button)

@bot.callback_query_handler(func=lambda call: True)
def characters_page_callback(call):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id)) == 'oz':
        if (call.data).split('_')[0] == 'activ':
            if UserCart.objects.filter(id=(call.data).split('_')[1], user__tg_id=call.message.chat.id, status=True, status_check=True):
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Faollashtirilgan')
            else:
                if int(TgUser.objects.filter(tg_id=call.message.chat.id)[0].balance) >= int(Paket.objects.filter(id=UserCart.objects.filter(id=(call.data).split('_')[1], user__tg_id=call.message.chat.id, status=False, status_check=True)[0].paket_id)[0].price):
                    from django.db.models import F
                    TgUser.objects.filter(tg_id=call.message.chat.id).update(balance=F('balance') - int(Paket.objects.filter(id=UserCart.objects.filter(id=(call.data).split('_')[1], user__tg_id=call.message.chat.id, status=False, status_check=True)[0].paket_id)[0].price))
                    UserCart.objects.filter(id=(call.data).split('_')[1], user__tg_id=call.message.chat.id, status=False, status_check=True).update(status=True)
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Faollashtirildi')
                else:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Hisobingizda mablag\' yetarli emas')

        elif (call.data).split('_')[0] == 'search':
            if PodCategory.objects.filter(oz=UserSearch.objects.get(tg_id=call.message.chat.id).podcategory):
                search_obj = UserCart.objects.filter(status=True, tuman=Tuman.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).tuman).id, viloyat=Viloyat.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).viloyat).id, avto=Avto.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=call.message.chat.id).avtokub).id, podcategory=PodCategory.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).podcategory).id, category=Category.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).category).id).order_by('-id')
            else:
                search_obj = UserCart.objects.filter(status=True, tuman=Tuman.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).tuman).id, viloyat=Viloyat.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).viloyat).id, avto=Avto.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=call.message.chat.id).avtokub).id, podcategory=None, category=Category.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).category).id)

            if int((call.data).split('_')[1]) == ceil(search_obj.count()/Service.get_count(Config.objects.all())):
                if PodCategory.objects.filter(oz=UserSearch.objects.get(tg_id=call.message.chat.id).podcategory):
                    search_obj = UserCart.objects.filter(status=True, tuman=Tuman.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).tuman).id, viloyat=Viloyat.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).viloyat).id, avto=Avto.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=call.message.chat.id).avtokub).id, podcategory=PodCategory.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).podcategory).id, category=Category.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).category).id).order_by('-id')
                else:
                    search_obj = UserCart.objects.filter(status=True, tuman=Tuman.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).tuman).id, viloyat=Viloyat.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).viloyat).id, avto=Avto.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=call.message.chat.id).avtokub).id, podcategory=None, category=Category.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).category).id)
                from django.core.paginator import Paginator
                paginator = Paginator(search_obj, Service.get_count(Config.objects.all()))
                search_object = paginator.get_page(int((call.data).split('_')[1]))
                for i in search_object:
                    if i.podcategory:
                        pcat =  i.podcategory.oz
                    else:
                        pcat = ''
                    if i.narx:
                        nnarx = i.narx
                    else:
                        nnarx = 'Kelishilgan narx'
                    if i.username:
                        usern = '@'+i.username
                    else:
                        usern = i.telefon
                    bot.send_message(call.message.chat.id, f'\nKategoriya: {i.category.oz}, {pcat}\nBoshlang\'ich narx: {nnarx}\nMoshina rusumi: {i.avto.oz}, {i.kub} kub\nViloyat: {i.viloyat.oz}, {i.tuman.oz}\nTelefon raqam: {i.telefon}\nTelegram: {usern}\n')

                btnsearch = types.InlineKeyboardMarkup()
                btnsearch.row(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['prev'], callback_data=f'search_{search_object.previous_page_number()}'))
                bot.send_message(call.message.chat.id, f'(1 /  {ceil(len(search_obj)/Service.get_count(Config.objects.all()))})', reply_markup=btnsearch)

            elif int((call.data).split('_')[1]) == 1:
                if PodCategory.objects.filter(oz=UserSearch.objects.get(tg_id=call.message.chat.id).podcategory):
                    search_obj = UserCart.objects.filter(status=True, tuman=Tuman.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).tuman).id, viloyat=Viloyat.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).viloyat).id, avto=Avto.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=call.message.chat.id).avtokub).id, podcategory=PodCategory.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).podcategory).id, category=Category.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).category).id).order_by('-id')
                else:
                    search_obj = UserCart.objects.filter(status=True, tuman=Tuman.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).tuman).id, viloyat=Viloyat.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).viloyat).id, avto=Avto.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=call.message.chat.id).avtokub).id, podcategory=None, category=Category.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).category).id)
                from django.core.paginator import Paginator
                paginator = Paginator(search_obj, Service.get_count(Config.objects.all()))
                search_object = paginator.get_page(int((call.data).split('_')[1]))
                for i in search_object:
                    if i.podcategory:
                        pcat =  i.podcategory.oz
                    else:
                        pcat = ''
                    if i.narx:
                        nnarx = i.narx
                    else:
                        nnarx = 'Kelishilgan narx'
                    if i.username:
                        usern = '@'+i.username
                    else:
                        usern = i.telefon
                    bot.send_message(call.message.chat.id, f'\nKategoriya: {i.category.oz}, {pcat}\nBoshlang\'ich narx: {nnarx}\nMoshina rusumi: {i.avto.oz}, {i.kub} kub\nViloyat: {i.viloyat.oz}, {i.tuman.oz}\nTelefon raqam: {i.telefon}\nTelegram: {usern}\n')

                btnsearch = types.InlineKeyboardMarkup()
                btnsearch.row(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['next_to'], callback_data=f'search_{search_object.next_page_number()}'))
                bot.send_message(call.message.chat.id, f'(1 /  {ceil(len(search_obj)/Service.get_count(Config.objects.all()))})', reply_markup=btnsearch)
            else:
                if PodCategory.objects.filter(oz=UserSearch.objects.get(tg_id=call.message.chat.id).podcategory):
                    search_obj = UserCart.objects.filter(status=True, tuman=Tuman.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).tuman).id, viloyat=Viloyat.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).viloyat).id, avto=Avto.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=call.message.chat.id).avtokub).id, podcategory=PodCategory.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).podcategory).id, category=Category.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).category).id).order_by('-id')
                else:
                    search_obj = UserCart.objects.filter(status=True, tuman=Tuman.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).tuman).id, viloyat=Viloyat.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).viloyat).id, avto=Avto.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=call.message.chat.id).avtokub).id, podcategory=None, category=Category.objects.get(oz=UserSearch.objects.get(tg_id=call.message.chat.id).category).id)
                from django.core.paginator import Paginator
                paginator = Paginator(search_obj, Service.get_count(Config.objects.all()))
                search_object = paginator.get_page(int((call.data).split('_')[1]))
                for i in search_object:
                    if i.podcategory:
                        pcat =  i.podcategory.oz
                    else:
                        pcat = ''
                    if i.narx:
                        nnarx = i.narx
                    else:
                        nnarx = 'Kelishilgan narx'
                    if i.username:
                        usern = '@'+i.username
                    else:
                        usern = i.telefon
                    bot.send_message(call.message.chat.id, f'\nKategoriya: {i.category.oz}, {pcat}\nBoshlang\'ich narx: {nnarx}\nMoshina rusumi: {i.avto.oz}, {i.kub} kub\nViloyat: {i.viloyat.oz}, {i.tuman.oz}\nTelefon raqam: {i.telefon}\nTelegram: {usern}\n')
                btnsearch = types.InlineKeyboardMarkup()
                btnsearch.row(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['next_to'], callback_data=f'search_{1}'))
                bot.send_message(call.message.chat.id, f'(1 /  {ceil(len(search_obj)/Service.get_count(Config.objects.all()))})', reply_markup=btnsearch)


        elif (call.data).split('_')[0] == 'post':
            if int((call.data).split('_')[1]) == ceil(UserCart.objects.filter(user__tg_id=call.message.chat.id).count()/Service.get_count(Config.objects.all())):
                from django.core.paginator import Paginator
                paginator = Paginator(UserCart.objects.filter(user__tg_id=call.message.chat.id, status_check=True), Service.get_count(Config.objects.all()))
                post_object = paginator.get_page(int((call.data).split('_')[1]))
                for i in post_object:
                    if i.podcategory:
                        pca = i.podcategory.oz
                    else:
                        pca = ''
                    if i.narx:
                        pna = i.narx
                    else:
                        pna = 'Kelishilgan narx'
                    if i.username:
                        una = '@'+i.username
                    else:
                        una = i.telefon
                    activ_button = types.InlineKeyboardMarkup(row_width=1)
                    activ_button.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['activ'], callback_data=f'activ_{i.id}'))
                    bot.send_message(call.message.chat.id, f'\nKategoriya: {i.category.oz}, {pca}\nBoshlang\'ich narx: {pna}\nMoshina rusumi: {i.avto.oz} {i.kub} kub\nViloyat: {i.viloyat.oz}, {i.tuman.oz}\nTelefon raqam: {i.telefon}\nTelegram: {una}\nTarif (paket): {i.paket.name_oz}', reply_markup=activ_button)
                btuz1 = types.InlineKeyboardMarkup()
                btuz1.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['prev'], callback_data=f'post_{post_object.previous_page_number()}'))
                bot.send_message(call.message.chat.id, f'({call.data.split("_")[1]} / {ceil(UserCart.objects.filter(user__tg_id=call.message.chat.id).count()/Service.get_count(Config.objects.all()))})', reply_markup=btuz1)
            elif int((call.data).split('_')[1]) == 1:
                from django.core.paginator import Paginator
                paginator = Paginator(UserCart.objects.filter(user__tg_id=call.message.chat.id, status_check=True), Service.get_count(Config.objects.all()))
                post_object = paginator.get_page(int((call.data).split('_')[1]))
                for i in post_object:
                    if i.podcategory:
                        pca = i.podcategory.oz
                    else:
                        pca = ''
                    if i.narx:
                        pna = i.narx
                    else:
                        pna = 'Kelishilgan narx'
                    if i.username:
                        una = '@'+i.username
                    else:
                        una = i.telefon
                    activ_button = types.InlineKeyboardMarkup(row_width=1)
                    activ_button.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['activ'], callback_data=f'activ_{i.id}'))
                    bot.send_message(call.message.chat.id, f'\nKategoriya: {i.category.oz}, {pca}\nBoshlang\'ich narx: {pna}\nMoshina rusumi: {i.avto.oz} {i.kub} kub\nViloyat: {i.viloyat.oz}, {i.tuman.oz}\nTelefon raqam: {i.telefon}\nTelegram: {una}\nTarif (paket): {i.paket.name_oz}', reply_markup=activ_button)
                btuz1 = types.InlineKeyboardMarkup()
                btuz1.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['next'], callback_data=f'post_{post_object.next_page_number()}'))
                bot.send_message(call.message.chat.id, f'({call.data.split("_")[1]} / {ceil(UserCart.objects.filter(user__tg_id=call.message.chat.id).count()/Service.get_count(Config.objects.all()))})', reply_markup=btuz1)
            else:
                from django.core.paginator import Paginator
                paginator = Paginator(UserCart.objects.filter(user__tg_id=call.message.chat.id, status_check=True), Service.get_count(Config.objects.all()))
                post_object = paginator.get_page(int((call.data).split('_')[1]))
                for i in post_object:
                    if i.podcategory:
                        pca = i.podcategory.oz
                    else:
                        pca = ''
                    if i.narx:
                        pna = i.narx
                    else:
                        pna = 'Kelishilgan narx'
                    if i.username:
                        una = '@'+i.username
                    else:
                        una = i.telefon
                    activ_button = types.InlineKeyboardMarkup(row_width=1)
                    activ_button.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['activ'], callback_data=f'activ_{i.id}'))
                    bot.send_message(call.message.chat.id, f'\nKategoriya: {i.category.oz}, {pca}\nBoshlang\'ich narx: {pna}\nMoshina rusumi: {i.avto.oz} {i.kub} kub\nViloyat: {i.viloyat.oz}, {i.tuman.oz}\nTelefon raqam: {i.telefon}\nTelegram: {una}\nTarif (paket): {i.paket.name_oz}', reply_markup=activ_button)
                btuz1 = types.InlineKeyboardMarkup()
                btuz1.row(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['prev'], callback_data=f'post_{post_object.previous_page_number()}'), types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['next_to'], callback_data=f'post_{post_object.next_page_number()}'))
                bot.send_message(call.message.chat.id, f'({call.data.split("_")[1]} / {ceil(UserCart.objects.filter(user__tg_id=call.message.chat.id).count()/Service.get_count(Config.objects.all()))})', reply_markup=btuz1)

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id)) == 'uz':
        if (call.data).split('_')[0] == 'activ':
            if UserCart.objects.filter(id=(call.data).split('_')[1], user__tg_id=call.message.chat.id, status=True, status_check=True):
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Фаоллаштирилган')
            else:
                if int(TgUser.objects.filter(tg_id=call.message.chat.id)[0].balance) >= int(Paket.objects.filter(id=UserCart.objects.filter(id=(call.data).split('_')[1], user__tg_id=call.message.chat.id, status=False, status_check=True)[0].paket_id)[0].price):
                    from django.db.models import F
                    TgUser.objects.filter(tg_id=call.message.chat.id).update(balance=F('balance') - int(Paket.objects.filter(id=UserCart.objects.filter(id=(call.data).split('_')[1], user__tg_id=call.message.chat.id, status=False, status_check=True)[0].paket_id)[0].price))
                    UserCart.objects.filter(id=(call.data).split('_')[1], user__tg_id=call.message.chat.id, status=False, status_check=True).update(status=True)
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Фаоллаштирилди')
                else:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Ҳисобингизда маблағ етарли эмас')

        elif (call.data).split('_')[0] == 'post':
            if int((call.data).split('_')[1]) == ceil(UserCart.objects.filter(user__tg_id=call.message.chat.id).count()/Service.get_count(Config.objects.all())):
                from django.core.paginator import Paginator
                paginator = Paginator(UserCart.objects.filter(user__tg_id=call.message.chat.id, status_check=True).order_by('-id'), Service.get_count(Config.objects.all()))
                post_object = paginator.get_page(int((call.data).split('_')[1]))
                for i in post_object:
                    if i.podcategory:
                        pca = i.podcategory.uz
                    else:
                        pca = ''
                    if i.narx:
                        pna = i.narx
                    else:
                        pna = 'Келишилган нарх'
                    if i.username:
                        una = '@'+i.username
                    else:
                        una = i.telefon
                    activ_button = types.InlineKeyboardMarkup(row_width=1)
                    activ_button.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['activ'], callback_data=f'activ_{i.id}'))
                    bot.send_message(call.message.chat.id, f'\nКатегория: {i.category.uz}, {pca}\nБошланғич нарх: {pna}\nМошина русуми: {i.avto.uz}, {i.kub} куб\nВилоят: {i.viloyat.uz}, {i.tuman.uz}\nТелефон рақам: {i.telefon}\nТелеграм: {una}\nТариф (пакет): {i.paket.name_uz}', reply_markup=activ_button)
                btuz1 = types.InlineKeyboardMarkup()
                btuz1.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['prev'], callback_data=f'post_{post_object.previous_page_number()}'))
                bot.send_message(call.message.chat.id, f'({call.data.split("_")[1]} / {ceil(UserCart.objects.filter(user__tg_id=call.message.chat.id).count()/Service.get_count(Config.objects.all()))})', reply_markup=btuz1)
            elif int((call.data).split('_')[1]) == 1:
                from django.core.paginator import Paginator
                paginator = Paginator(UserCart.objects.filter(user__tg_id=call.message.chat.id, status_check=True).order_by('-id'), Service.get_count(Config.objects.all()))
                post_object = paginator.get_page(int((call.data).split('_')[1]))
                for i in post_object:
                    if i.podcategory:
                        pca = i.podcategory.uz
                    else:
                        pca = ''
                    if i.narx:
                        pna = i.narx
                    else:
                        pna = 'Келишилган нарх'
                    if i.username:
                        una = '@'+i.username
                    else:
                        una = i.telefon
                    activ_button = types.InlineKeyboardMarkup(row_width=1)
                    activ_button.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['activ'], callback_data=f'activ_{i.id}'))
                    bot.send_message(call.message.chat.id, f'\nКатегория: {i.category.uz}, {pca}\nБошланғич нарх: {pna}\nМошина русуми: {i.avto.uz}, {i.kub} куб\nВилоят: {i.viloyat.uz}, {i.tuman.uz}\nТелефон рақам: {i.telefon}\nТелеграм: {una}\nТариф (пакет): {i.paket.name_uz}', reply_markup=activ_button)
                btuz1 = types.InlineKeyboardMarkup()
                btuz1.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['next'], callback_data=f'post_{post_object.next_page_number()}'))
                bot.send_message(call.message.chat.id, f'({call.data.split("_")[1]} / {ceil(UserCart.objects.filter(user__tg_id=call.message.chat.id).count()/Service.get_count(Config.objects.all()))})', reply_markup=btuz1)
            else:
                from django.core.paginator import Paginator
                paginator = Paginator(UserCart.objects.filter(user__tg_id=call.message.chat.id, status_check=True).order_by('-id'), Service.get_count(Config.objects.all()))
                post_object = paginator.get_page(int((call.data).split('_')[1]))
                for i in post_object:
                    if i.podcategory:
                        pca = i.podcategory.uz
                    else:
                        pca = ''
                    if i.narx:
                        pna = i.narx
                    else:
                        pna = 'Келишилган нарх'
                    if i.username:
                        una = '@'+i.username
                    else:
                        una = i.telefon
                    activ_button = types.InlineKeyboardMarkup(row_width=1)
                    activ_button.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['activ'], callback_data=f'activ_{i.id}'))
                    bot.send_message(call.message.chat.id, f'\nКатегория: {i.category.uz}, {pca}\nБошланғич нарх: {pna}\nМошина русуми: {i.avto.uz}, {i.kub} куб\nВилоят: {i.viloyat.uz}, {i.tuman.uz}\nТелефон рақам: {i.telefon}\nТелеграм: {una}\nТариф (пакет): {i.paket.name_uz}', reply_markup=activ_button)
                btuz1 = types.InlineKeyboardMarkup()
                btuz1.row(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['prev'], callback_data=f'post_{post_object.previous_page_number()}'), types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['next_to'], callback_data=f'post_{post_object.next_page_number()}'))
                bot.send_message(call.message.chat.id, f'({call.data.split("_")[1]} / {ceil(UserCart.objects.filter(user__tg_id=call.message.chat.id).count()/Service.get_count(Config.objects.all()))})', reply_markup=btuz1)
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id)) == 'ru':
        if (call.data).split('_')[0] == 'activ':
            if UserCart.objects.filter(id=(call.data).split('_')[1], user__tg_id=call.message.chat.id, status=True, status_check=True):
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Активирован')
            else:
                if int(TgUser.objects.filter(tg_id=call.message.chat.id)[0].balance) >= int(Paket.objects.filter(id=UserCart.objects.filter(id=(call.data).split('_')[1], user__tg_id=call.message.chat.id, status=False, status_check=True)[0].paket_id)[0].price):
                    from django.db.models import F
                    TgUser.objects.filter(tg_id=call.message.chat.id).update(balance=F('balance') - int(Paket.objects.filter(id=UserCart.objects.filter(id=(call.data).split('_')[1], user__tg_id=call.message.chat.id, status=False, status_check=True)[0].paket_id)[0].price))
                    UserCart.objects.filter(id=(call.data).split('_')[1], user__tg_id=call.message.chat.id, status=False, status_check=True).update(status=True)
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Активирован')
                else:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='На вашем счету недостаточно денег')

        elif (call.data).split('_')[0] == 'post':
            if int((call.data).split('_')[1]) == ceil(UserCart.objects.filter(user__tg_id=call.message.chat.id).count()/Service.get_count(Config.objects.all())):
                from django.core.paginator import Paginator
                paginator = Paginator(UserCart.objects.filter(user__tg_id=call.message.chat.id, status_check=True), Service.get_count(Config.objects.all()))
                post_object = paginator.get_page(int((call.data).split('_')[1]))
                for i in post_object:
                    if i.podcategory:
                        pca = i.podcategory.ru
                    else:
                        pca = ''
                    if i.narx:
                        pna = i.narx
                    else:
                        pna = 'Цена договорная'
                    if i.username:
                        una = '@'+i.username
                    else:
                        una = i.telefon
                    activ_button = types.InlineKeyboardMarkup(row_width=1)
                    activ_button.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['activ'], callback_data=f'activ_{i.id}'))
                    bot.send_message(call.message.chat.id, f'\nКатегория: {i.category.ru}, {pca}\nНачальная цена: {pna}\nМарка машины: {i.avto.ru}, {i.kub} куб\nОбласть: {i.viloyat.ru}, {i.tuman.ru}\nНомер телефона: {i.telefon}\nТелеграм: {una}\nТариф (пакет): {i.paket.name_ru}', reply_markup=activ_button)
                btuz1 = types.InlineKeyboardMarkup()
                btuz1.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['prev'], callback_data=f'post_{post_object.previous_page_number()}'))
                bot.send_message(call.message.chat.id, f'({call.data.split("_")[1]} / {ceil(UserCart.objects.filter(user__tg_id=call.message.chat.id).count()/Service.get_count(Config.objects.all()))})', reply_markup=btuz1)
            elif int((call.data).split('_')[1]) == 1:
                from django.core.paginator import Paginator
                paginator = Paginator(UserCart.objects.filter(user__tg_id=call.message.chat.id, status_check=True), Service.get_count(Config.objects.all()))
                post_object = paginator.get_page(int((call.data).split('_')[1]))
                for i in post_object:
                    if i.podcategory:
                        pca = i.podcategory.ru
                    else:
                        pca = ''
                    if i.narx:
                        pna = i.narx
                    else:
                        pna = 'Цена договорная'
                    if i.username:
                        una = '@'+i.username
                    else:
                        una = i.telefon
                    activ_button = types.InlineKeyboardMarkup(row_width=1)
                    activ_button.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['activ'], callback_data=f'activ_{i.id}'))
                    bot.send_message(call.message.chat.id, f'\nКатегория: {i.category.ru}, {pca}\nНачальная цена: {pna}\nМарка машины: {i.avto.ru}, {i.kub} куб\nОбласть: {i.viloyat.ru}, {i.tuman.ru}\nНомер телефона: {i.telefon}\nТелеграм: {una}\nТариф (пакет): {i.paket.name_ru}', reply_markup=activ_button)
                btuz1 = types.InlineKeyboardMarkup()
                btuz1.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['next'], callback_data=f'post_{post_object.next_page_number()}'))
                bot.send_message(call.message.chat.id, f'({call.data.split("_")[1]} / {ceil(UserCart.objects.filter(user__tg_id=call.message.chat.id).count()/Service.get_count(Config.objects.all()))})', reply_markup=btuz1)
            else:
                from django.core.paginator import Paginator
                paginator = Paginator(UserCart.objects.filter(user__tg_id=call.message.chat.id, status_check=True), Service.get_count(Config.objects.all()))
                post_object = paginator.get_page(int((call.data).split('_')[1]))
                for i in post_object:
                    if i.podcategory:
                        pca = i.podcategory.ru
                    else:
                        pca = ''
                    if i.narx:
                        pna = i.narx
                    else:
                        pna = 'Цена договорная'
                    if i.username:
                        una = '@'+i.username
                    else:
                        una = i.telefon
                    activ_button = types.InlineKeyboardMarkup(row_width=1)
                    activ_button.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['activ'], callback_data=f'activ_{i.id}'))
                    bot.send_message(call.message.chat.id, f'\nКатегория: {i.category.ru}, {pca}\nНачальная цена: {pna}\nМарка машины: {i.avto.ru}, {i.kub} куб\nОбласть: {i.viloyat.ru}, {i.tuman.ru}\nНомер телефона: {i.telefon}\nТелеграм: {una}\nТариф (пакет): {i.paket.name_ru}', reply_markup=activ_button)
                btuz1 = types.InlineKeyboardMarkup()
                btuz1.row(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['prev'], callback_data=f'post_{post_object.previous_page_number()}'), types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['next_to'], callback_data=f'post_{post_object.next_page_number()}'))
                bot.send_message(call.message.chat.id, f'({call.data.split("_")[1]} / {ceil(UserCart.objects.filter(user__tg_id=call.message.chat.id).count()/Service.get_count(Config.objects.all()))})', reply_markup=btuz1)



@bot.message_handler(func=lambda msg: msg.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=msg.from_user.id))]['my_post'])
def send_profile(message):
    if UserCart.objects.filter(user__tg_id=message.from_user.id).exists():
        if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
            from django.core.paginator import Paginator
            paginator = Paginator(UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=True).order_by('-id'), Service.get_count(Config.objects.all()))
            post_object = paginator.get_page(1)
            btuz = types.InlineKeyboardMarkup()
            for i in post_object:
                if i.podcategory:
                    pcat =  i.podcategory.oz
                else:
                    pcat = ''
                if i.narx:
                    nnarx = i.narx
                else:
                    nnarx = 'Kelishilgan narx'
                if i.username:
                    usern = '@'+i.username
                else:
                    usern = i.telefon

                activ_button = types.InlineKeyboardMarkup()
                activ_button.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['activ'], callback_data=f'activ_{i.id}'))
                bot.send_message(message.from_user.id, f'\nKategoriya: {i.category.oz}, {pcat}\nBoshlang\'ich narx: {nnarx}\nMoshina rusumi: {i.avto.oz}, {i.kub} kub\nViloyat: {i.viloyat.oz}, {i.tuman.oz}\nTelefon raqam: {i.telefon}\nTelegram: {usern}\nTarif (paket): {i.paket.name_oz}', reply_markup=activ_button)
            btuz.row(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['next_to'], callback_data=f'post_{post_object.next_page_number()}'))
            bot.send_message(message.from_user.id, f'(1 / {ceil(UserCart.objects.filter(user__tg_id=message.from_user.id).count()/Service.get_count(Config.objects.all()))})', reply_markup=btuz)

        elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
            from django.core.paginator import Paginator
            paginator = Paginator(UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=True).order_by('-id'), Service.get_count(Config.objects.all()))
            post_object = paginator.get_page(1)
            btuz = types.InlineKeyboardMarkup()
            for i in post_object:
                if i.podcategory:
                    pcat =  i.podcategory.uz
                else:
                    pcat = ''
                if i.narx:
                    nnarx = i.narx
                else:
                    nnarx = 'Келишилган нарх'
                if i.username:
                    usern = '@'+i.username
                else:
                    usern = i.telefon
                activ_button = types.InlineKeyboardMarkup()
                activ_button.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['activ'], callback_data=f'activ_{i.id}'))
                bot.send_message(message.from_user.id, f'\nКатегория: {i.category.uz}, {pcat}\nБошланғич нарх: {nnarx}\nМошина русуми: {i.avto.uz}, {i.kub} куб\nВилоят: {i.viloyat.uz}, {i.tuman.uz}\nТелефон рақам: {i.telefon}\nТелеграм: {usern}\nТариф (пакет): {i.paket.name_uz}', reply_markup=activ_button)
            btuz.row(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['next_to'], callback_data=f'post_{post_object.next_page_number()}'))
            bot.send_message(message.from_user.id, f'(1 / {ceil(UserCart.objects.filter(user__tg_id=message.from_user.id).count()/Service.get_count(Config.objects.all()))})', reply_markup=btuz)

        elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
            from django.core.paginator import Paginator
            paginator = Paginator(UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=True).order_by('-id'), Service.get_count(Config.objects.all()))
            post_object = paginator.get_page(1)
            btuz = types.InlineKeyboardMarkup()
            for i in post_object:
                if i.podcategory:
                    pcat =  i.podcategory.ru
                else:
                    pcat = ''
                if i.narx:
                    nnarx = i.narx
                else:
                    nnarx = 'Цена договорная'
                if i.username:
                    usern = '@'+i.username
                else:
                    usern = i.telefon

                activ_button = types.InlineKeyboardMarkup()
                activ_button.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['activ'], callback_data=f'activ_{i.id}'))
                bot.send_message(message.from_user.id, f'\nКатегория: {i.category.ru}, {pcat}\nНачальная цена: {nnarx}\nМарка машины: {i.avto.ru}, {i.kub} куб\nОбласть: {i.viloyat.ru}, {i.tuman.ru}\nНомер телефона: {i.telefon}\nТелеграм: {usern}\nТариф (пакет): {i.paket.name_ru}', reply_markup=activ_button)
            btuz.row(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['next_to'], callback_data=f'post_{post_object.next_page_number()}'))
            bot.send_message(message.from_user.id, f'(1 / {ceil(UserCart.objects.filter(user__tg_id=message.from_user.id).count()/Service.get_count(Config.objects.all()))})', reply_markup=btuz)

    else:
        bot.send_message(message.chat.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['post_not'], reply_markup=home_func(message))





@bot.message_handler(func=lambda msg: msg.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=msg.chat.id))]['balance'])
def balance(message):
    pass

@bot.message_handler(func=lambda msg: msg.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=msg.chat.id))]['profile'])
def send_profile(message):
    bot.send_message(message.chat.id, 'profile')

@bot.message_handler(func=lambda msg: msg.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=msg.chat.id))]['info'])
def get_info(message):
    info_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    info_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['about']), types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['contacts']))
    info_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['edit_lan']))
    info_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['home']))
    bot.send_message(message.chat.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['info'], reply_markup=info_button)


@bot.message_handler(func=lambda msg: msg.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=msg.chat.id))]['homeback'])
def get_homeback(message):
    start_handler(message)

@bot.message_handler(func=lambda msg: msg.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=msg.chat.id))]['home'])
def get_home(message):
    start_handler(message)

@bot.message_handler(func=lambda msg: msg.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=msg.chat.id))]['about'])
def get_about(message):
    about_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    about_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['home']))
    from botconfig.models import Config
    for i in Config.objects.filter(lan=Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))):
        bot.send_message(message.chat.id, i.about, reply_markup=about_button)

@bot.message_handler(func=lambda msg: msg.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=msg.chat.id))]['contacts'])
def get_contact(message):
    contacts_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    contacts_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['home']))
    from botconfig.models import Config
    for i in Config.objects.filter(lan=Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))):
        bot.send_message(message.chat.id, i.contact, reply_markup=contacts_button)

@bot.message_handler(func=lambda msg: msg.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=msg.chat.id))]['addavto'])
def get_addavto(message):
    if UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False):
        UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).delete()
        user_lan = Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))
        add_avto_replay_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn = []
        if Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id)) == 'oz':
            TgUser.objects.filter(tg_id=message.chat.id).update(step=USER_STEP['ADD_AVTO'])
            for j in Category.objects.all():
                btn.append(types.KeyboardButton(text=j.oz))
        elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id)) == 'uz':
            TgUser.objects.filter(tg_id=message.chat.id).update(step=USER_STEP['ADD_AVTO'])
            for j in Category.objects.all():
                btn.append(types.KeyboardButton(text=j.uz))
        elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id)) == 'ru':
            TgUser.objects.filter(tg_id=message.chat.id).update(step=USER_STEP['ADD_AVTO'])
            for j in Category.objects.all():
                btn.append(types.KeyboardButton(text=j.ru))
    else:
        user_lan = Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))
        add_avto_replay_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn = []
        if Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id)) == 'oz':
            TgUser.objects.filter(tg_id=message.chat.id).update(step=USER_STEP['ADD_AVTO'])
            for j in Category.objects.all():
                btn.append(types.KeyboardButton(text=j.oz))
        elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id)) == 'uz':
            TgUser.objects.filter(tg_id=message.chat.id).update(step=USER_STEP['ADD_AVTO'])
            for j in Category.objects.all():
                btn.append(types.KeyboardButton(text=j.uz))
        elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id)) == 'ru':
            TgUser.objects.filter(tg_id=message.chat.id).update(step=USER_STEP['ADD_AVTO'])
            for j in Category.objects.all():
                btn.append(types.KeyboardButton(text=j.ru))


    add_avto_replay_button.add(*btn)
    add_avto_replay_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['home']))
    bot.send_message(message.chat.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['service'], reply_markup=add_avto_replay_button)

@bot.message_handler(func=lambda msg: msg.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=msg.chat.id))]['whouse'])
def get_whouse(message):
    addavto_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    addavto_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['home']))
    for i in Config.objects.filter(lan=Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))):
        bot.send_message(message.chat.id, i.whouse, reply_markup=addavto_button)

@bot.message_handler(func=lambda msg: msg.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=msg.chat.id))]['edit_lan'])
def get_edit_lan(message):
    TgUser.objects.filter(tg_id=message.chat.id).update(step=USER_STEP['EDIT_LAN'])
    lan_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    lan_button.add((types.KeyboardButton(text='🇺🇿 O\'zbek')), (types.KeyboardButton(text='🇺🇿 Узбек')), (types.KeyboardButton(text='🇷🇺 Руский')))
    lan_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['back']), types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['home']))
    bot.send_message(message.chat.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['edit_lan'], reply_markup=lan_button)

@bot.message_handler(func=lambda msg: msg.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=msg.chat.id))]['search'])
def get_search(message):
    from . models import UserSearch
    if UserSearch.objects.filter(tg_id=message.from_user.id):
        UserSearch.objects.filter(tg_id=message.from_user.id).delete()
        if Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id)) == 'oz':
            search_button_oz = []
            for j in Category.objects.all():
                search_button_oz.append(types.KeyboardButton(text=j.oz))

            search_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            search_button.add(*search_button_oz)
            search_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['home']))
            bot.send_message(message.chat.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['search_what1'], reply_markup=search_button)
            TgUser.objects.filter(tg_id=message.chat.id).update(step=USER_STEP['SEARCH'])

        elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id)) == 'uz':
            search_button_uz = []
            for j in Category.objects.all():
                search_button_uz.append(types.KeyboardButton(text=j.uz))

            search_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            search_button.add(*search_button_uz)
            search_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['home']))
            bot.send_message(message.chat.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['search_what1'], reply_markup=search_button)
            TgUser.objects.filter(tg_id=message.chat.id).update(step=USER_STEP['SEARCH'])

        elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id)) == 'ru':
            search_button_ru = []
            for j in Category.objects.all():
                search_button_ru.append(types.KeyboardButton(text=j.ru))

            search_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            search_button.add(*search_button_ru)
            search_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['home']))
            bot.send_message(message.chat.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['search_what1'], reply_markup=search_button)
            TgUser.objects.filter(tg_id=message.chat.id).update(step=USER_STEP['SEARCH'])
    else:
        if Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id)) == 'oz':
            search_button_oz = []
            for j in Category.objects.all():
                search_button_oz.append(types.KeyboardButton(text=j.oz))

            search_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            search_button.add(*search_button_oz)
            search_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['home']))
            bot.send_message(message.chat.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['search_what1'], reply_markup=search_button)
            TgUser.objects.filter(tg_id=message.chat.id).update(step=USER_STEP['SEARCH'])

        elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id)) == 'uz':
            search_button_uz = []
            for j in Category.objects.all():
                search_button_uz.append(types.KeyboardButton(text=j.uz))

            search_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            search_button.add(*search_button_uz)
            search_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['home']))
            bot.send_message(message.chat.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['search_what1'], reply_markup=search_button)
            TgUser.objects.filter(tg_id=message.chat.id).update(step=USER_STEP['SEARCH'])

        elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id)) == 'ru':
            search_button_ru = []
            for j in Category.objects.all():
                search_button_ru.append(types.KeyboardButton(text=j.ru))

            search_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            search_button.add(*search_button_ru)
            search_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['home']))
            bot.send_message(message.chat.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.chat.id))]['search_what1'], reply_markup=search_button)
            TgUser.objects.filter(tg_id=message.chat.id).update(step=USER_STEP['SEARCH'])





@bot.message_handler(content_types=['text', 'contact'])
def text_handler(message):
    switcher = {
        USER_STEP['LAN']: enter_lan,
        USER_STEP['DEFAULT']: select_category,
        USER_STEP['EDIT_LAN']: update_lan,
        USER_STEP['ADD_AVTO']: get_pod,
        USER_STEP['GET_POD_CATEGORY']: get_avto_name,
        USER_STEP['GET_KUB']: get_avto_kub,
        USER_STEP['GET_VILOYAT']: get_viloyat,
        USER_STEP['GET_TUMAN']: tuman,
        USER_STEP['GET_NARX']: paket,
        USER_STEP['GET_TEL']: get_tel,
        USER_STEP['GET_N']: narx,
        USER_STEP['CHECK']: check,
        USER_STEP['FINAL']: final,
        #### search ####
        USER_STEP['SEARCH']: search,
        USER_STEP['SEARCH_AVTO_KUB']: search_avto_kub,
        USER_STEP['SEARCH_VILOYAT']: search_viloyat,
        USER_STEP['SEARCH_TUMAN']: search_tuman,
        USER_STEP['SEARCH_RESULT']: search_result,
        USER_STEP['SEARCH_POD']: search_avto_list

    }
    print("qadam=> ", TgUser.objects.get(tg_id=message.chat.id).step)
    func = switcher.get(TgUser.objects.get(tg_id=message.chat.id).step, lambda: start_handler(message))
    func(message, bot)





















    #########################
