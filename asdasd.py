elif (call.data).split('_')[0] == 'search':
    if PodCategory.objects.filter(ru=UserSearch.objects.get(tg_id=call.message.chat.id).podcategory):
        search_obj = UserCart.objects.filter(status=1, tuman=Tuman.objects.get(ru=UserSearch.objects.get(tg_id=call.message.chat.id).tuman).id, viloyat=Viloyat.objects.get(ru=UserSearch.objects.get(tg_id=call.message.chat.id).viloyat).id, avto=Avto.objects.get(ru=UserSearch.objects.get(tg_id=call.message.chat.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=call.message.chat.id).avtokub).id, podcategory=PodCategory.objects.get(ru=UserSearch.objects.get(tg_id=call.message.chat.id).podcategory).id, category=Category.objects.get(ru=UserSearch.objects.get(tg_id=call.message.chat.id).category).id).order_by('-id')
    else:
        search_obj = UserCart.objects.filter(status=1, tuman=Tuman.objects.get(ru=UserSearch.objects.get(tg_id=call.message.chat.id).tuman).id, viloyat=Viloyat.objects.get(ru=UserSearch.objects.get(tg_id=call.message.chat.id).viloyat).id, avto=Avto.objects.get(ru=UserSearch.objects.get(tg_id=call.message.chat.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=call.message.chat.id).avtokub).id, podcategory=None, category=Category.objects.get(ru=UserSearch.objects.get(tg_id=call.message.chat.id).category).id).order_by('-id')

    if int((call.data).split('_')[1]) == ceil(len(search_obj)/Service.get_count(Config.objects.all())):
        from django.core.paginator import Paginator
        paginator = Paginator(search_obj, Service.get_count(Config.objects.all()))
        post_object = paginator.get_page(int((call.data).split('_')[1]))
        for i in post_object:
            if i.podcategory:
                pca = i.podcategory.ru
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

            bot.send_message(call.message.chat.id, f'\nKategoriya: {i.category.ru}, {pca}\nBoshlang\'ich narx: {pna}\nMoshina rusumi: {i.avto.ru} {i.kub} kub\nViloyat: {i.viloyat.ru}, {i.tuman.ru}\nTelefon raqam: {i.telefon}\nTelegram: {una}')

        btru1 = types.InlineKeyboardMarkup()
        btru1.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['prev'], callback_data=f'search_{post_object.previous_page_number()}'))
        bot.send_message(call.message.chat.id, f'({call.data.split("_")[1]} / {ceil(search_obj.count()/Service.get_count(Config.objects.all()))})', reply_markup=btru1)
    elif int((call.data).split('_')[1]) == 1:
        from django.core.paginator import Paginator
        paginator = Paginator(search_obj, Service.get_count(Config.objects.all()))
        post_object = paginator.get_page(int((call.data).split('_')[1]))
        for i in post_object:
            if i.podcategory:
                pca = i.podcategory.ru
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

            bot.send_message(call.message.chat.id, f'\nКатегория: {i.category.ru}, {pca}\nБошланғич нарх: {pna}\nМошина русуми: {i.avto.ru}, {i.kub} куб\nВилоят: {i.viloyat.ru}, {i.tuman.ru}\nТелефон рақам: {i.telefon}\nТелеграм: {una}\nТариф (пакет): {i.paket.name_ru}')
        btru1 = types.InlineKeyboardMarkup()
        btru1.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['next'], callback_data=f'search_{post_object.next_page_number()}'))
        bot.send_message(call.message.chat.id, f'({call.data.split("_")[1]} / {ceil(search_obj.count()/Service.get_count(Config.objects.all()))})', reply_markup=btru1)
    else:
        from django.core.paginator import Paginator
        paginator = Paginator(search_obj, Service.get_count(Config.objects.all()))
        post_object = paginator.get_page(int((call.data).split('_')[1]))
        for i in post_object:
            if i.podcategory:
                pca = i.podcategory.ru
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
            bot.send_message(call.message.chat.id, f'\nКатегория: {i.category.ru}, {pca}\nБошланғич нарх: {pna}\nМошина русуми: {i.avto.ru}, {i.kub} куб\nВилоят: {i.viloyat.ru}, {i.tuman.ru}\nТелефон рақам: {i.telefon}\nТелеграм: {una}\nТариф (пакет): {i.paket.name_ru}')
        btru1 = types.InlineKeyboardMarkup()
        btru1.row(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['prev'], callback_data=f'search_{post_object.previous_page_number()}'), types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['next_to'], callback_data=f'search_{post_object.next_page_number()}'))
        bot.send_message(call.message.chat.id, f'({call.data.split("_")[1]} / {ceil(search_obj.count()/Service.get_count(Config.objects.all()))})', reply_markup=btru1)
