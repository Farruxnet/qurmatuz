import telebot
from telebot import types
from . models import TgUser, UserCart
from . const import LAN, USER_STEP
from django.conf import settings
from botconfig.models import PodCategory, Category, Avto, AvtoKub, Viloyat, Tuman, StartNarx, Paket
from . service import Service
from . models import UserSearch

def search(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        searchobj = UserSearch()
        searchobj.tg_id = message.from_user.id
        searchobj.category = message.text
        searchobj.save()
        if PodCategory.objects.filter(category=Category.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id, status=False).category).id):
            pod_cat_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            buttons = [types.KeyboardButton(text=text.oz) for text in PodCategory.objects.filter(category=Category.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id, status=False).category))]
            pod_cat_button.add(*buttons)
            pod_cat_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['service_pod'], reply_markup=pod_cat_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_POD'])
        else:
            try:
                btn = []
                for j in Avto.objects.all():
                    btn.append(types.KeyboardButton(text=j.oz))
                add_avto_replay_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                add_avto_replay_button.add(*btn)
                add_avto_replay_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
                bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['service'], reply_markup=add_avto_replay_button)
                TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_AVTO_KUB'])
            except:
                bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])


    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        pass
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        pass

def search_avto_list(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        try:

            UserSearch.objects.filter(tg_id=message.from_user.id).update(podcategory=message.text)
            btn = []
            for j in Avto.objects.all():
                btn.append(types.KeyboardButton(text=j.oz))
            add_avto_replay_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            add_avto_replay_button.add(*btn)
            add_avto_replay_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['service'], reply_markup=add_avto_replay_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_AVTO_KUB'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        pass
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        pass

def search_avto_kub(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        UserSearch.objects.filter(tg_id=message.from_user.id).update(avto=message.text)

        btnkuboz = []
        kub_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for i in Avto.objects.all().filter(oz=message.text):
            for j in i.kub.all():
                btnkuboz.append(types.KeyboardButton(text=str(j)))
        kub_button.add(*btnkuboz)
        kub_button.add(types.KeyboardButton(text=LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
        bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['select_avto_kub'], reply_markup=kub_button)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_VILOYAT'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        UserSearch.objects.filter(tg_id=message.from_user.id).update(avto=message.text)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_VILOYAT'])
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        UserSearch.objects.filter(tg_id=message.from_user.id).update(avto=message.text)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_VILOYAT'])

def search_viloyat(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        UserSearch.objects.filter(tg_id=message.from_user.id).update(avtokub=message.text)
        viloyat_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(kub=Service.get_id(AvtoKub.objects.filter(kub=message.text)))
        btn = []
        for i in Viloyat.objects.all().filter(status=True):
            btn.append(types.KeyboardButton(text=i.oz))

        viloyat_button.add(*btn)
        viloyat_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
        bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['select_viloyat'], reply_markup=viloyat_button)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_TUMAN'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        pass
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        pass

def search_tuman(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        UserSearch.objects.filter(tg_id=message.from_user.id).update(viloyat=message.text)
        btn = []
        print(UserSearch.objects.get(tg_id=message.from_user.id).viloyat)
        for j in Tuman.objects.filter(viloyat=Viloyat.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).viloyat).id):
            btn.append(types.KeyboardButton(text=j.oz))
        tuman_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        tuman_button.add(*btn)
        tuman_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
        bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['select_viloyat'], reply_markup=tuman_button)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_NARX'])
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        pass
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        pass

def search_narx(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        UserSearch.objects.filter(tg_id=message.from_user.id).update(tuman=message.text)
        btnnarx = []
        for narx in StartNarx.objects.all():
            btnnarx.append(types.KeyboardButton(text=narx.narx))
        narx_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        narx_button.add(*btnnarx)
        narx_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['kelishilgan']))
        narx_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
        bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['start_price']+'So\'m', reply_markup=narx_button)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_RESULT'])


    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        pass
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        pass

def search_result(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        from django.db.models import Q
        if message.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['kelishilgan']:
            search_object = UserCart.objects.filter(
                (Q(category=Category.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).category).id) | Q(podcategory=PodCategory.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).podcategory).id)) &
                (Q(avto=Avto.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).avto).id) | Q(kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=message.from_user.id).avtokub))) &
                (Q(viloyat=Viloyat.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).viloyat)) | Q(tuman=Tuman.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).tuman))) & Q(narx=None)
            )
            if search_object:
                for i in search_object:
                    bot.send_message(message.from_user.id, i.viloyat.oz)
            else:
                bot.send_message(message.from_user.id, 'Topilmadi')

        else:
            UserSearch.objects.filter(tg_id=message.from_user.id).update(narx=message.text)
            search_object = UserCart.objects.filter(
                (Q(category=Category.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).category).id) | Q(podcategory=PodCategory.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).podcategory).id)) &
                (Q(avto=Avto.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).avto).id) | Q(kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=message.from_user.id).avtokub))) &
                (Q(viloyat=Viloyat.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).viloyat)) | Q(tuman=Tuman.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).tuman))) & Q(narx=StartNarx.objects.get(narx=UserSearch.objects.get(tg_id=message.from_user.id).narx))
            )
            if search_object:
                for i in search_object:
                    bot.send_message(message.from_user.id, i.viloyat.oz)


            else:
                bot.send_message(message.from_user.id, 'Topilmadi')

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        pass
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        pass







###############################
