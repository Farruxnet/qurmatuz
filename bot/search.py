import telebot
from telebot import types
from . models import TgUser, UserCart
from . const import LAN, USER_STEP
from django.conf import settings
from botconfig.models import PodCategory, Category, Avto, AvtoKub, Viloyat, Tuman, StartNarx, Paket, Config
from . service import Service
from . models import UserSearch
from math import ceil
def search(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        searchobj = UserSearch()
        searchobj.tg_id = message.from_user.id
        searchobj.category = message.text
        searchobj.save()
        if PodCategory.objects.filter(category=Category.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).category).id):
            pod_cat_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            buttons = [types.KeyboardButton(text=text.oz) for text in PodCategory.objects.filter(category=Category.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).category))]
            pod_cat_button.add(*buttons)
            pod_cat_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_pod1'], reply_markup=pod_cat_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_POD'])
        else:
            try:
                btn = []
                for j in Avto.objects.all():
                    btn.append(types.KeyboardButton(text=j.oz))
                add_avto_replay_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                add_avto_replay_button.add(*btn)
                add_avto_replay_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
                bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_avto1'], reply_markup=add_avto_replay_button)
                TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_AVTO_KUB'])
            except:
                bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])


    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        searchobj = UserSearch()
        searchobj.tg_id = message.from_user.id
        searchobj.category = message.text
        searchobj.save()
        if PodCategory.objects.filter(category=Category.objects.get(uz=UserSearch.objects.get(tg_id=message.from_user.id).category).id):
            pod_cat_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            buttons = [types.KeyboardButton(text=text.uz) for text in PodCategory.objects.filter(category=Category.objects.get(uz=UserSearch.objects.get(tg_id=message.from_user.id).category))]
            pod_cat_button.add(*buttons)
            pod_cat_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_pod1'], reply_markup=pod_cat_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_POD'])
        else:
            try:
                btn = []
                for j in Avto.objects.all():
                    btn.append(types.KeyboardButton(text=j.uz))
                add_avto_replay_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                add_avto_replay_button.add(*btn)
                add_avto_replay_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
                bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_avto1'], reply_markup=add_avto_replay_button)
                TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_AVTO_KUB'])
            except:
                bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        searchobj = UserSearch()
        searchobj.tg_id = message.from_user.id
        searchobj.category = message.text
        searchobj.save()
        if PodCategory.objects.filter(category=Category.objects.get(ru=UserSearch.objects.get(tg_id=message.from_user.id).category).id):
            pod_cat_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            buttons = [types.KeyboardButton(text=text.ru) for text in PodCategory.objects.filter(category=Category.objects.get(ru=UserSearch.objects.get(tg_id=message.from_user.id).category))]
            pod_cat_button.add(*buttons)
            pod_cat_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_pod1'], reply_markup=pod_cat_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_POD'])
        else:
            try:
                btn = []
                for j in Avto.objects.all():
                    btn.append(types.KeyboardButton(text=j.ru))
                add_avto_replay_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                add_avto_replay_button.add(*btn)
                add_avto_replay_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
                bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_avto1'], reply_markup=add_avto_replay_button)
                TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_AVTO_KUB'])
            except:
                bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])


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
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_avto1'], reply_markup=add_avto_replay_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_AVTO_KUB'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        try:
            UserSearch.objects.filter(tg_id=message.from_user.id).update(podcategory=message.text)
            btn = []
            for j in Avto.objects.all():
                btn.append(types.KeyboardButton(text=j.uz))
            add_avto_replay_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            add_avto_replay_button.add(*btn)
            add_avto_replay_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_avto1'], reply_markup=add_avto_replay_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_AVTO_KUB'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        try:
            UserSearch.objects.filter(tg_id=message.from_user.id).update(podcategory=message.text)
            btn = []
            for j in Avto.objects.all():
                btn.append(types.KeyboardButton(text=j.ru))
            add_avto_replay_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            add_avto_replay_button.add(*btn)
            add_avto_replay_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_avto1'], reply_markup=add_avto_replay_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_AVTO_KUB'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

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
        bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_avto_kub1'], reply_markup=kub_button)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_VILOYAT'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        UserSearch.objects.filter(tg_id=message.from_user.id).update(avto=message.text)

        btnkuboz = []
        kub_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for i in Avto.objects.all().filter(uz=message.text):
            for j in i.kub.all():
                btnkuboz.append(types.KeyboardButton(text=str(j)))
        kub_button.add(*btnkuboz)
        kub_button.add(types.KeyboardButton(text=LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
        bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_avto_kub1'], reply_markup=kub_button)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_VILOYAT'])
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        UserSearch.objects.filter(tg_id=message.from_user.id).update(avto=message.text)
        btnkuboz = []
        kub_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for i in Avto.objects.all().filter(ru=message.text):
            for j in i.kub.all():
                btnkuboz.append(types.KeyboardButton(text=str(j)))
        kub_button.add(*btnkuboz)
        kub_button.add(types.KeyboardButton(text=LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
        bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_avto_kub1'], reply_markup=kub_button)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_VILOYAT'])

def search_viloyat(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        UserSearch.objects.filter(tg_id=message.from_user.id).update(avtokub=message.text)
        viloyat_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn = []
        for i in Viloyat.objects.all().filter(status=True):
            btn.append(types.KeyboardButton(text=i.oz))

        viloyat_button.add(*btn)
        viloyat_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
        bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_viloyat1'], reply_markup=viloyat_button)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_TUMAN'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        UserSearch.objects.filter(tg_id=message.from_user.id).update(avtokub=message.text)
        viloyat_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn = []
        for i in Viloyat.objects.all().filter(status=True):
            btn.append(types.KeyboardButton(text=i.uz))

        viloyat_button.add(*btn)
        viloyat_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
        bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_viloyat1'], reply_markup=viloyat_button)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_TUMAN'])
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        UserSearch.objects.filter(tg_id=message.from_user.id).update(avtokub=message.text)
        viloyat_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn = []
        for i in Viloyat.objects.all().filter(status=True):
            btn.append(types.KeyboardButton(text=i.ru))

        viloyat_button.add(*btn)
        viloyat_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
        bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_viloyat1'], reply_markup=viloyat_button)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_TUMAN'])

def search_tuman(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        UserSearch.objects.filter(tg_id=message.from_user.id).update(viloyat=message.text)
        btn = []
        for j in Tuman.objects.filter(viloyat=Viloyat.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).viloyat).id):
            btn.append(types.KeyboardButton(text=j.oz))
        tuman_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        tuman_button.add(*btn)
        tuman_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
        bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_tuman1'], reply_markup=tuman_button)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_RESULT'])
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        UserSearch.objects.filter(tg_id=message.from_user.id).update(viloyat=message.text)
        btn = []
        for j in Tuman.objects.filter(viloyat=Viloyat.objects.get(uz=UserSearch.objects.get(tg_id=message.from_user.id).viloyat).id):
            btn.append(types.KeyboardButton(text=j.uz))
        tuman_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        tuman_button.add(*btn)
        tuman_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
        bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_tuman1'], reply_markup=tuman_button)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_RESULT'])
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        UserSearch.objects.filter(tg_id=message.from_user.id).update(viloyat=message.text)
        btn = []
        for j in Tuman.objects.filter(viloyat=Viloyat.objects.get(ru=UserSearch.objects.get(tg_id=message.from_user.id).viloyat).id):
            btn.append(types.KeyboardButton(text=j.ru))
        tuman_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        tuman_button.add(*btn)
        tuman_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
        bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search_tuman1'], reply_markup=tuman_button)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['SEARCH_RESULT'])


def search_result(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        from django.db.models import Q
        from django.core.paginator import Paginator
        UserSearch.objects.filter(tg_id=message.from_user.id).update(tuman=message.text)
        if PodCategory.objects.filter(oz=UserSearch.objects.get(tg_id=message.from_user.id).podcategory):
            search_obj = UserCart.objects.filter(status=1, tuman=Tuman.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).tuman).id, viloyat=Viloyat.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).viloyat).id, avto=Avto.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=message.from_user.id).avtokub).id, podcategory=PodCategory.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).podcategory).id, category=Category.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).category).id).order_by('-id')
            paginator = Paginator(search_obj, Service.get_count(Config.objects.all()))
            search_object = paginator.get_page(1)
        else:
            search_obj = UserCart.objects.filter(status=1, tuman=Tuman.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).tuman).id, viloyat=Viloyat.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).viloyat).id, avto=Avto.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=message.from_user.id).avtokub).id, podcategory=None, category=Category.objects.get(oz=UserSearch.objects.get(tg_id=message.from_user.id).category).id)
            paginator = Paginator(search_obj, Service.get_count(Config.objects.all()))
            search_object = paginator.get_page(1)

        if search_object:
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
                bot.send_message(message.from_user.id, f'\n<b>Kategoriya:</b> {i.category.oz}, {pcat}\n<b>Boshlang\'ich narx:</b> {nnarx}\n<b>Moshina rusumi</b>: {i.avto.oz}, {i.kub} kub\n<b>Viloyat</b>: {i.viloyat.oz}, {i.tuman.oz}\n\n☎️ {i.telefon}\n\n✏️ {usern}', parse_mode="HTML")


            btnsearch = types.InlineKeyboardMarkup()
            btnsearch.row(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['next_to'], callback_data=f'search_{search_object.next_page_number()}'))
            bot.send_message(message.from_user.id, f'(1 /  {ceil(len(search_obj)/Service.get_count(Config.objects.all()))})', reply_markup=btnsearch)
        else:
            bot.send_message(message.from_user.id, 'Siz kiritgan ma\'lumotlar bo\'yicha topilmadi')

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        from django.db.models import Q
        from django.core.paginator import Paginator
        UserSearch.objects.filter(tg_id=message.from_user.id).update(tuman=message.text)
        if PodCategory.objects.filter(uz=UserSearch.objects.get(tg_id=message.from_user.id).podcategory):
            search_obj = UserCart.objects.filter(status=1, tuman=Tuman.objects.get(uz=UserSearch.objects.get(tg_id=message.from_user.id).tuman).id, viloyat=Viloyat.objects.get(uz=UserSearch.objects.get(tg_id=message.from_user.id).viloyat).id, avto=Avto.objects.get(uz=UserSearch.objects.get(tg_id=message.from_user.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=message.from_user.id).avtokub).id, podcategory=PodCategory.objects.get(uz=UserSearch.objects.get(tg_id=message.from_user.id).podcategory).id, category=Category.objects.get(uz=UserSearch.objects.get(tg_id=message.from_user.id).category).id).order_by('-id')
            paginator = Paginator(search_obj, Service.get_count(Config.objects.all()))
            search_object = paginator.get_page(1)
        else:
            search_obj = UserCart.objects.filter(status=1, tuman=Tuman.objects.get(uz=UserSearch.objects.get(tg_id=message.from_user.id).tuman).id, viloyat=Viloyat.objects.get(uz=UserSearch.objects.get(tg_id=message.from_user.id).viloyat).id, avto=Avto.objects.get(uz=UserSearch.objects.get(tg_id=message.from_user.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=message.from_user.id).avtokub).id, podcategory=None, category=Category.objects.get(uz=UserSearch.objects.get(tg_id=message.from_user.id).category).id)
            paginator = Paginator(search_obj, Service.get_count(Config.objects.all()))
            search_object = paginator.get_page(1)

        if search_object:
            for i in search_object:
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
                bot.send_message(message.from_user.id, f'\n<b>Категория:</b> {i.category.uz}, {pcat}\n<b>Бошланғич нарх:</b> {nnarx}\n<b>Мошина русуми:</b> {i.avto.uz}, {i.kub} куб\n<b>Вилоят:</b> {i.viloyat.uz}, {i.tuman.uz}\n\n☎️ {i.telefon}\n\n✏️ {usern}\n', parse_mode="HTML")

            btnsearch = types.InlineKeyboardMarkup()
            btnsearch.row(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['next_to'], callback_data=f'search_{search_object.next_page_number()}'))
            bot.send_message(message.from_user.id, f'(1 /  {ceil(len(search_obj)/Service.get_count(Config.objects.all()))})', reply_markup=btnsearch)
        else:
            bot.send_message(message.from_user.id, 'Сиз киритган маълумотлар бўйича топилмади')

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        from django.db.models import Q
        from django.core.paginator import Paginator
        UserSearch.objects.filter(tg_id=message.from_user.id).update(tuman=message.text)
        if PodCategory.objects.filter(ru=UserSearch.objects.get(tg_id=message.from_user.id).podcategory):
            search_obj = UserCart.objects.filter(status=1, tuman=Tuman.objects.get(ru=UserSearch.objects.get(tg_id=message.from_user.id).tuman).id, viloyat=Viloyat.objects.get(ru=UserSearch.objects.get(tg_id=message.from_user.id).viloyat).id, avto=Avto.objects.get(ru=UserSearch.objects.get(tg_id=message.from_user.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=message.from_user.id).avtokub).id, podcategory=PodCategory.objects.get(ru=UserSearch.objects.get(tg_id=message.from_user.id).podcategory).id, category=Category.objects.get(ru=UserSearch.objects.get(tg_id=message.from_user.id).category).id).order_by('-id')
            paginator = Paginator(search_obj, Service.get_count(Config.objects.all()))
            search_object = paginator.get_page(1)
        else:
            search_obj = UserCart.objects.filter(status=1, tuman=Tuman.objects.get(ru=UserSearch.objects.get(tg_id=message.from_user.id).tuman).id, viloyat=Viloyat.objects.get(ru=UserSearch.objects.get(tg_id=message.from_user.id).viloyat).id, avto=Avto.objects.get(ru=UserSearch.objects.get(tg_id=message.from_user.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=message.from_user.id).avtokub).id, podcategory=None, category=Category.objects.get(ru=UserSearch.objects.get(tg_id=message.from_user.id).category).id)
            paginator = Paginator(search_obj, Service.get_count(Config.objects.all()))
            search_object = paginator.get_page(1)

        if search_object:
            for i in search_object:
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
                bot.send_message(message.from_user.id, f'\n<b>Категория:</b> {i.category.ru}, {pcat}\n<b>Начальная цена:</b> {nnarx}\n<b>Марка машины:</b> {i.avto.ru}, {i.kub} куб\n<b>Область:</b> {i.viloyat.ru}, {i.tuman.ru}\n\n☎️ {i.telefon}\n\n✏️ {usern}\n', parse_mode="HTML")

            btnsearch = types.InlineKeyboardMarkup()
            btnsearch.row(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['next_to'], callback_data=f'search_{search_object.next_page_number()}'))
            bot.send_message(message.from_user.id, f'(1 /  {ceil(len(search_obj)/Service.get_count(Config.objects.all()))})', reply_markup=btnsearch)
        else:
            bot.send_message(message.from_user.id, 'Не найдено согласно введенной вами информации')









###############################
