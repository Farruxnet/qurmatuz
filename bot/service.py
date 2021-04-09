import telebot
from telebot import types
from . models import TgUser, UserCart
from . const import LAN, USER_STEP
from django.conf import settings
from botconfig.models import PodCategory, Category, Avto, AvtoKub, Viloyat, Tuman, StartNarx, Paket
# 1 - search notifications server orqali bash script bilan
# 2 - deatline delete server orqali bash script bilan

class Service:
    def get_user_lan(object):
        id = 0
        for i in object:
            id = i.lan
        return id
    def get_id(obj):
        id = 0
        for j in obj:
            id = j.id
        return id

    def get_count(obj):
        c = 0
        for j in obj:
            c = j.list_count
        return c


def home_func(message):
    home_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    home_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['search']), types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['addavto']), types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['info']), types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['whouse']))
    home_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['my_post']), types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['balance']))
    return home_button


# Tilni tanlash
def enter_lan(message, bot):
    if message.text == '🇺🇿 O\'zbek':
        TgUser.objects.filter(tg_id=message.from_user.id).update(lan='oz', step=USER_STEP['DEFAULT'])
        bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['homename'], reply_markup=home_func(message))
    elif message.text == '🇺🇿 Узбек':
        TgUser.objects.filter(tg_id=message.from_user.id).update(lan='uz', step=USER_STEP['DEFAULT'])
        bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['homename'], reply_markup=home_func(message))
    elif message.text == '🇷🇺 Руский':
        TgUser.objects.filter(tg_id=message.from_user.id).update(lan='ru', step=USER_STEP['DEFAULT'])
        bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['homename'], reply_markup=home_func(message))
    else:
        TgUser.objects.filter(tg_id=message.from_user.id).update(lan='uz', step=USER_STEP['DEFAULT'])
        bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['homename'], reply_markup=home_func(message))

# Tilni o'zgartirish
def update_lan(message, bot):
    if message.text == '🇺🇿 O\'zbek':
        TgUser.objects.filter(tg_id=message.from_user.id).update(lan='oz', step=USER_STEP['DEFAULT'])
        bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['homename'], reply_markup=home_func(message))
    elif message.text == '🇺🇿 Узбек':
        TgUser.objects.filter(tg_id=message.from_user.id).update(lan='uz', step=USER_STEP['DEFAULT'])
        bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['homename'], reply_markup=home_func(message))
    elif message.text == '🇷🇺 Руский':
        TgUser.objects.filter(tg_id=message.from_user.id).update(lan='ru', step=USER_STEP['DEFAULT'])
        bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['homename'], reply_markup=home_func(message))
    elif message.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['back']:
        bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['homename'], reply_markup=home_func(message))
    else:
        TgUser.objects.filter(tg_id=message.from_user.id).update(lan='uz', step=USER_STEP['DEFAULT'])
        bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['homename'], reply_markup=home_func(message))

# bosh sahifa
def select_category(message, bot):
    bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['homename'], reply_markup=home_func(message))

def get_pod(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        try:
            user_add = UserCart()
            user_add.user = TgUser.objects.get(tg_id=message.from_user.id)
            user_add.category = Category.objects.get(oz=message.text)
            user_add.save()
            if PodCategory.objects.filter(category=Category.objects.get(oz=UserCart.objects.get(user__tg_id=message.from_user.id, status_check=False).category.oz).id):
                pod_cat_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                for i in UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False):
                    for y in Category.objects.filter(oz=i.category.oz):
                        buttons = [types.KeyboardButton(text=text.oz) for text in PodCategory.objects.filter(category=y.id)]
                pod_cat_button.add(*buttons)
                pod_cat_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
                bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['service_pod'], reply_markup=pod_cat_button)
                TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_POD_CATEGORY'])
            else:
                try:
                    btn = []
                    for j in Avto.objects.all():
                        btn.append(types.KeyboardButton(text=j.oz))
                    add_avto_replay_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                    add_avto_replay_button.add(*btn)
                    add_avto_replay_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
                    bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['service'], reply_markup=add_avto_replay_button)
                    TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_KUB'])
                except:
                    bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])



        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        try:
            user_add = UserCart()
            user_add.user = TgUser.objects.get(tg_id=message.from_user.id)
            user_add.category = Category.objects.get(uz=message.text)
            user_add.save()
            if PodCategory.objects.filter(category=Category.objects.get(uz=UserCart.objects.get(user__tg_id=message.from_user.id, status_check=False).category.uz).id):
                pod_cat_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                for i in UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False):
                    for y in Category.objects.filter(uz=i.category.uz):
                        buttons = [types.KeyboardButton(text=text.uz) for text in PodCategory.objects.filter(category=y.id)]

                pod_cat_button.add(*buttons)
                pod_cat_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
                bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['service_pod'], reply_markup=pod_cat_button)
                TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_POD_CATEGORY'])
            else:
                try:
                    btn = []
                    for j in Avto.objects.all():
                        btn.append(types.KeyboardButton(text=j.uz))
                    add_avto_replay_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                    add_avto_replay_button.add(*btn)
                    add_avto_replay_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
                    bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['service'], reply_markup=add_avto_replay_button)
                    TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_KUB'])
                except:
                    bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        try:
            user_add = UserCart()
            user_add.user = TgUser.objects.get(tg_id=message.from_user.id)
            user_add.category = Category.objects.get(ru=message.text)
            user_add.save()
            if PodCategory.objects.filter(category=Category.objects.get(ru=UserCart.objects.get(user__tg_id=message.from_user.id, status_check=False).category.ru).id):
                pod_cat_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                for i in UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False):
                    for y in Category.objects.filter(ru=i.category.ru):
                        buttons = [types.KeyboardButton(text=text.ru) for text in PodCategory.objects.filter(category=y.id)]

                pod_cat_button.add(*buttons)
                pod_cat_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
                bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['service_pod'], reply_markup=pod_cat_button)
                TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_POD_CATEGORY'])
            else:
                try:
                    btnru = []
                    for j in Avto.objects.all():
                        btnru.append(types.KeyboardButton(text=j.ru))
                    add_avto_replay_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                    add_avto_replay_button.add(*btnru)
                    add_avto_replay_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
                    bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['service'], reply_markup=add_avto_replay_button)
                    TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_KUB'])
                except:
                    bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

def get_avto_name(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        try:
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(podcategory=Service.get_id(PodCategory.objects.filter(oz=message.text)))
            btn = []
            for j in Avto.objects.all():
                btn.append(types.KeyboardButton(text=j.oz))
            add_avto_replay_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            add_avto_replay_button.add(*btn)
            add_avto_replay_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['service'], reply_markup=add_avto_replay_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_KUB'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        try:
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(podcategory=Service.get_id(PodCategory.objects.filter(uz=message.text)))
            btn = []
            for j in Avto.objects.all():
                btn.append(types.KeyboardButton(text=j.uz))
            add_avto_replay_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            add_avto_replay_button.add(*btn)
            add_avto_replay_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['service'], reply_markup=add_avto_replay_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_KUB'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        try:
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(podcategory=Service.get_id(PodCategory.objects.filter(ru=message.text)))
            btn = []
            for j in Avto.objects.all():
                btn.append(types.KeyboardButton(text=j.ru))
            add_avto_replay_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            add_avto_replay_button.add(*btn)
            add_avto_replay_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['service'], reply_markup=add_avto_replay_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_KUB'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])


# avtomobillar sigimi chiqariladi
def get_avto_kub(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        try:
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(avto=Avto.objects.get(oz=message.text))
            btn = []
            kub_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            for i in Avto.objects.all().filter(oz=message.text):
                for j in i.kub.all():
                    btn.append(types.KeyboardButton(text=str(j)))
            kub_button.add(*btn)
            kub_button.add(types.KeyboardButton(text=LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['select_avto_kub'], reply_markup=kub_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_VILOYAT'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        try:
            btn = []
            kub_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(avto=Avto.objects.get(uz=message.text))
            for i in Avto.objects.all().filter(uz=message.text):
                for j in i.kub.all():
                    btn.append(types.KeyboardButton(text=str(j)))
            kub_button.add(*btn)
            kub_button.add(types.KeyboardButton(text=LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['select_avto_kub'], reply_markup=kub_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_VILOYAT'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        try:
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(avto=Avto.objects.get(ru=message.text))
            btn = []
            kub_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            for i in Avto.objects.all().filter(ru=message.text):
                for j in i.kub.all():
                    btn.append(types.KeyboardButton(text=str(j)))
            kub_button.add(*btn)
            kub_button.add(types.KeyboardButton(text=LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['select_avto_kub'], reply_markup=kub_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_VILOYAT'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])


def get_viloyat(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        try:
            viloyat_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(kub=Service.get_id(AvtoKub.objects.filter(kub=message.text)))
            btn = []
            for i in Viloyat.objects.all().filter(status=True):
                btn.append(types.KeyboardButton(text=i.oz))

            viloyat_button.add(*btn)
            viloyat_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['select_viloyat'], reply_markup=viloyat_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_TUMAN'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        try:
            viloyat_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(kub=Service.get_id(AvtoKub.objects.filter(kub=message.text)))
            btn = []
            for i in Viloyat.objects.all().filter(status=True):
                btn.append(types.KeyboardButton(text=i.uz))

            viloyat_button.add(*btn)
            viloyat_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['select_viloyat'], reply_markup=viloyat_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_TUMAN'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        try:
            viloyat_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(kub=Service.get_id(AvtoKub.objects.filter(kub=message.text)))
            btn = []
            for i in Viloyat.objects.all().filter(status=True):
                btn.append(types.KeyboardButton(text=i.ru))

            viloyat_button.add(*btn)
            viloyat_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['select_viloyat'], reply_markup=viloyat_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_TUMAN'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])


def tuman(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        try:
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(viloyat=Viloyat.objects.get(oz=message.text))
            btn = []
            for d in UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False):
                for j in Tuman.objects.filter(viloyat=d.viloyat):
                    btn.append(types.KeyboardButton(text=j.oz))
            tuman_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            tuman_button.add(*btn)
            tuman_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['select_viloyat'], reply_markup=tuman_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_NARX'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        try:
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(viloyat=Viloyat.objects.get(uz=message.text))
            btn = []
            for d in UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False):
                for j in Tuman.objects.filter(viloyat=d.viloyat):
                    btn.append(types.KeyboardButton(text=j.uz))
            tuman_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            tuman_button.add(*btn)
            tuman_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['select_viloyat'], reply_markup=tuman_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_NARX'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        try:
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(viloyat=Viloyat.objects.get(ru=message.text))
            btn = []
            for d in UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False):
                for j in Tuman.objects.filter(viloyat=d.viloyat):
                    btn.append(types.KeyboardButton(text=j.ru))
            tuman_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            tuman_button.add(*btn)
            tuman_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[ Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['select_viloyat'], reply_markup=tuman_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_NARX'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

def paket(message, bot):
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        try:
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(tuman=Tuman.objects.get(oz=message.text))
            paket_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btntel = []
            for i in Paket.objects.all():
                btntel.append(types.KeyboardButton(text=i.name_oz))
            paket_button.add(*btntel)
            paket_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['select_plan'], reply_markup=paket_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_N'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        try:
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(tuman=Tuman.objects.get(uz=message.text))
            paket_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btntel = []
            for i in Paket.objects.all():
                btntel.append(types.KeyboardButton(text=i.name_uz))
            paket_button.add(*btntel)
            paket_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['select_plan'], reply_markup=paket_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_N'])

        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        try:
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(tuman=Tuman.objects.get(ru=message.text))
            paket_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btntel = []
            for i in Paket.objects.all():
                btntel.append(types.KeyboardButton(text=i.name_ru))
            paket_button.add(*btntel)
            paket_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['select_plan'], reply_markup=paket_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_N'])

        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])





def narx(message, bot):
    import datetime
    from django.utils import timezone
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        for j in Paket.objects.filter(name_oz=message.text):
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(paket=j.id, deatline=(timezone.now()+datetime.timedelta(days=j.day)))
        btnnarx = []
        for narx in StartNarx.objects.all():
            btnnarx.append(types.KeyboardButton(text=narx.narx))
        narx_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        narx_button.add(*btnnarx)
        narx_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['kelishilgan']))
        narx_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
        bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['start_price']+'So\'m', reply_markup=narx_button)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_TEL'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        for j in Paket.objects.filter(name_uz=message.text):
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(paket=j.id, deatline=(timezone.now()+datetime.timedelta(days=j.day)))
        btnnarx = []
        for narx in StartNarx.objects.all():
            btnnarx.append(types.KeyboardButton(text=narx.narx))
        narx_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        narx_button.add(*btnnarx)
        narx_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['kelishilgan']))
        narx_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
        bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['start_price']+'So\'m', reply_markup=narx_button)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_TEL'])
    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        for j in Paket.objects.filter(name_ru=message.text):
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(paket=j.id, deatline=(timezone.now()+datetime.timedelta(days=j.day)))
        btnnarx = []
        for narx in StartNarx.objects.all():
            btnnarx.append(types.KeyboardButton(text=narx.narx))
        narx_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        narx_button.add(*btnnarx)
        narx_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['kelishilgan']))
        narx_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
        bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['start_price']+' So\'m', reply_markup=narx_button)
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['GET_TEL'])

def get_tel(message, bot):
    try:
        if message.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['kelishilgan']:
            tel_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            tel_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['tel'], request_contact=True))
            tel_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['send_tel'], reply_markup=tel_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['FINAL'])
        else:
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(narx=Service.get_id(StartNarx.objects.filter(narx=message.text)))
            tel_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            tel_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['tel'], request_contact=True))
            tel_button.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['home']))
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['send_tel'], reply_markup=tel_button)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['FINAL'])
    except:
        bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])



def final(message, bot):
    import datetime
    if Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'oz':
        try:
            if '+' in message.contact.phone_number:
                tel_check = message.contact.phone_number
            else:
                tel_check = '+'+message.contact.phone_number
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(telefon=tel_check, username=message.from_user.username)
            for ioz in UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False, status=False):
                cat = ioz.category.oz
                nar = ioz.narx
                if ioz.podcategory:
                    podcat =  ioz.podcategory.oz
                else:
                    podcat = ''
                if ioz.narx:
                    nar = ioz.narx
                else:
                    nar = 'Kelishilgan narx'
                if ioz.username:
                    username = '@'+ioz.username
                else:
                    username = ioz.telefon
                avto = ioz.avto.oz
                kub = ioz.kub
                viloyat = ioz.viloyat.oz
                tuman = ioz.tuman.oz
                telefon = ioz.telefon
                paket = ioz.paket.name_oz
            done_buttonoz = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            done_buttonoz.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['yes']), types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['no']))
            bot.send_message(message.from_user.id, f'Kiritgan ma\'lumotlaringiz to\'g\'rimi?\n\nKategoriya: {cat}, {podcat}\nBoshlang\'ich narx: {nar}\nMoshina rusumi: {avto} {kub} kub\nViloyat: {viloyat}, {tuman}\nTelefon raqam: {telefon}\nTelegram: {username}\nTarif (paket): {paket}\n', reply_markup=done_buttonoz)

            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['CHECK'])

        except:
            if '+' in message.text:
                tel_check2 = message.text
            else:
                tel_check2 = '+'+message.text
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(telefon=tel_check2, username=message.from_user.username)
            for ioz in UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False, status=False):
                cat = ioz.category.oz
                nar = ioz.narx
                if ioz.podcategory:
                    podcat =  ioz.podcategory.oz
                else:
                    podcat = ''
                if ioz.narx:
                    nar = ioz.narx
                else:
                    nar = 'Kelishilgan narx'
                if ioz.username:
                    username = '@'+ioz.username
                else:
                    username = ioz.telefon
                avto = ioz.avto.oz
                kub = ioz.kub
                viloyat = ioz.viloyat.oz
                tuman = ioz.tuman.oz
                telefon = ioz.telefon
                paket = ioz.paket.name_oz

            done_buttonoz = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            done_buttonoz.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['yes']), types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['no']))
            bot.send_message(message.from_user.id, f'Kiritgan ma\'lumotlaringiz to\'g\'rimi?\n\nKategoriya: {cat}, {podcat}\nBoshlang\'ich narx: {nar}\nMoshina rusumi: {avto} {kub} kub\nViloyat: {viloyat}, {tuman}\nTelefon raqam: {telefon}\nTelegram: {username}\nTarif (paket): {paket}\n', reply_markup=done_buttonoz)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['CHECK'])

    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'uz':
        try:
            if '+' in message.contact.phone_number:
                tel_check = message.contact.phone_number
            else:
                tel_check = '+'+message.contact.phone_number
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(telefon=tel_check, username=message.from_user.username)
            for iuz in UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False, status=False):
                cat = iuz.category.uz
                nar = iuz.narx
                if iuz.podcategory:
                    podcat =  iuz.podcategory.uz
                else:
                    podcat = ''
                if iuz.narx:
                    nar = iuz.narx
                else:
                    nar = 'Келишилган нарх'
                if iuz.username:
                    username = '@'+iuz.username
                else:
                    username = iuz.telefon
                avto = iuz.avto.uz
                kub = iuz.kub
                viloyat = iuz.viloyat.uz
                tuman = iuz.tuman.uz
                telefon = iuz.telefon
                paket = iuz.paket.name_uz
            done_buttonuz = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            done_buttonuz.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['yes']), types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['no']))
            bot.send_message(message.from_user.id, f'Киритган маълумотларингиз тўғрими?\n\nКатегория: {cat}, {podcat}\nБошланғич нарх: {nar}\nМошина русуми: {avto} {kub} куб\nВилоят: {viloyat}, {tuman}\nТелефон рақам: {telefon}\nТелеграм: {username}\nТариф (пакет): {paket}\n', reply_markup=done_buttonuz)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['CHECK'])
        except:
            if '+' in message.text:
                tel_check2 = message.text
            else:
                tel_check2 = '+'+message.text
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(telefon=tel_check2, username=message.from_user.username)
            for iuz in UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False, status=False):
                cat = iuz.category.uz
                nar = iuz.narx
                if iuz.podcategory:
                    podcat =  iuz.podcategory.uz
                else:
                    podcat = ''
                if iuz.narx:
                    nar = iuz.narx
                else:
                    nar = 'Келишилган нарх'
                if iuz.username:
                    username = '@'+iuz.username
                else:
                    username = iuz.telefon
                avto = iuz.avto.uz
                kub = iuz.kub
                viloyat = iuz.viloyat.uz
                tuman = iuz.tuman.uz
                telefon = iuz.telefon
                paket = iuz.paket.name_uz
            done_buttonuz = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            done_buttonuz.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['yes']), types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['no']))
            bot.send_message(message.from_user.id, f'Киритган маълумотларингиз тўғрими?\n\nКатегория: {cat}, {podcat}\nБошланғич нарх: {nar}\nМошина русуми: {avto} {kub} куб\nВилоят: {viloyat}, {tuman}\nТелефон рақам: {telefon}\nТелеграм: {username}\nТариф (пакет): {paket}\n', reply_markup=done_buttonuz)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['CHECK'])



    elif Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id)) == 'ru':
        try:
            if '+' in message.contact.phone_number:
                tel_check = message.contact.phone_number
            else:
                tel_check = '+'+message.contact.phone_number
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(telefon=tel_check, username=message.from_user.username)
            for iru in UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False, status=False):
                cat = iru.category.ru
                nar = iru.narx
                if iru.podcategory:
                    podcat =  iru.podcategory.ru
                else:
                    podcat = ''
                if iru.narx:
                    nar = iru.narx
                else:
                    nar = 'Цена договорная'
                if iru.username:
                    username = '@'+iru.username
                else:
                    username = iru.telefon
                avto = iru.avto.ru
                kub = iru.kub
                viloyat = iru.viloyat.ru
                tuman = iru.tuman.ru
                telefon = iru.telefon
                paket = iru.paket.name_ru
            done_buttonru = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            done_buttonru.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['yes']), types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['no']))
            bot.send_message(message.from_user.id, f'Правильная ли информация, которую вы ввели?\n\nКатегория: {cat}, {podcat}\nНачальная цена: {nar}\nМарка машины: {avto}, {kub} куб\nОбласть: {viloyat}, {tuman}\nНомер телефона: {telefon}\nТелеграм: {username}\nТариф (paket): {paket}\n', reply_markup=done_buttonru)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['CHECK'])
        except:
            if message.text in '+':
                tel_check2 = message.text
            else:
                tel_check2 = '+'+message.text
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(telefon=tel_check2, username=message.from_user.username)
            for iru in UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False, status=False):
                cat = iru.category.ru
                nar = iru.narx
                if iru.podcategory:
                    podcat =  iru.podcategory.ru
                else:
                    podcat = ''
                if iru.narx:
                    nar = iru.narx
                else:
                    nar = 'Цена договорная'
                if iru.username:
                    username = '@'+iru.username
                else:
                    username = iru.telefon
                avto = iru.avto.ru
                kub = iru.kub
                viloyat = iru.viloyat.ru
                tuman = iru.tuman.ru
                telefon = iru.telefon
                paket = iru.paket.name_ru
            done_buttonru = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            done_buttonru.add(types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['yes']), types.KeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['no']))
            bot.send_message(message.from_user.id, f'Правильная ли информация, которую вы ввели?\n\nКатегория: {cat}, {podcat}\nНачальная цена: {nar}\nМарка машины: {avto}, {kub} куб\nОбласть: {viloyat}, {tuman}\nНомер телефона: {telefon}\nТелеграм: {username}\nТариф (paket): {paket}\n', reply_markup=done_buttonru)
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['CHECK'])




def check(message, bot):
    if message.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['yes']:
        UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).update(status_check=True)
        bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['success_add'], reply_markup=home_func(message))
        TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['DEFAULT'])
        if int(TgUser.objects.filter(tg_id=message.from_user.id)[0].balance) >= int(Paket.objects.filter(id=UserCart.objects.filter(user__tg_id=message.from_user.id, status=False, status_check=True)[0].paket_id)[0].price):
            from django.db.models import F
            TgUser.objects.filter(tg_id=message.from_user.id).update(balance=F('balance') - int(Paket.objects.filter(id=UserCart.objects.filter(user__tg_id=message.from_user.id, status=False, status_check=True)[0].paket_id)[0].price))
            UserCart.objects.filter(user__tg_id=message.from_user.id, status=False, status_check=True).update(status=True)
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['activ_ok'])
        else:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['act'])


    elif message.text == LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['no']:
        try:
            UserCart.objects.filter(user__tg_id=message.from_user.id, status_check=False).delete()
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['success_delete'], reply_markup=home_func(message))
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['DEFAULT'])
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])
    else:
        try:
            TgUser.objects.filter(tg_id=message.from_user.id).update(step=USER_STEP['DEFAULT'])
            bot.send_message(message.from_user.id, "XATOLIK", reply_markup=home_func(message))
        except:
            bot.send_message(message.from_user.id, LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=message.from_user.id))]['error'])





#################
