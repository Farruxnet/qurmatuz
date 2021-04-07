elif (call.data).split('_')[0] == 'search':
    if PodCategory.objects.filter(uz=UserSearch.objects.get(tg_id=call.message.chat.id).podcategory):
        search_obj = UserCart.objects.filter(status=1, tuman=Tuman.objects.get(uz=UserSearch.objects.get(tg_id=call.message.chat.id).tuman).id, viloyat=Viloyat.objects.get(uz=UserSearch.objects.get(tg_id=call.message.chat.id).viloyat).id, avto=Avto.objects.get(uz=UserSearch.objects.get(tg_id=call.message.chat.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=call.message.chat.id).avtokub).id, podcategory=PodCategory.objects.get(uz=UserSearch.objects.get(tg_id=call.message.chat.id).podcategory).id, category=Category.objects.get(uz=UserSearch.objects.get(tg_id=call.message.chat.id).category).id).order_by('-id')
    else:
        search_obj = UserCart.objects.filter(status=1, tuman=Tuman.objects.get(uz=UserSearch.objects.get(tg_id=call.message.chat.id).tuman).id, viloyat=Viloyat.objects.get(uz=UserSearch.objects.get(tg_id=call.message.chat.id).viloyat).id, avto=Avto.objects.get(uz=UserSearch.objects.get(tg_id=call.message.chat.id).avto).id, kub=AvtoKub.objects.get(kub=UserSearch.objects.get(tg_id=call.message.chat.id).avtokub).id, podcategory=None, category=Category.objects.get(uz=UserSearch.objects.get(tg_id=call.message.chat.id).category).id).order_by('-id')

    if int((call.data).split('_')[1]) == ceil(len(search_obj)/Service.get_count(Config.objects.all())):
        from django.core.paginator import Paginator
        paginator = Paginator(search_obj, Service.get_count(Config.objects.all()))
        post_object = paginator.get_page(int((call.data).split('_')[1]))
        for i in post_object:
            if i.podcategory:
                pca = i.podcategory.uz
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

            bot.send_message(call.message.chat.id, f'\nKategoriya: {i.category.uz}, {pca}\nBoshlang\'ich narx: {pna}\nMoshina rusumi: {i.avto.uz} {i.kub} kub\nViloyat: {i.viloyat.uz}, {i.tuman.uz}\nTelefon raqam: {i.telefon}\nTelegram: {una}')

        btuz1 = types.InlineKeyboardMarkup()
        btuz1.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['prev'], callback_data=f'search_{post_object.previous_page_number()}'))
        bot.send_message(call.message.chat.id, f'({call.data.split("_")[1]} / {ceil(search_obj.count()/Service.get_count(Config.objects.all()))})', reply_markup=btuz1)
    elif int((call.data).split('_')[1]) == 1:
        from django.core.paginator import Paginator
        paginator = Paginator(search_obj, Service.get_count(Config.objects.all()))
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

            bot.send_message(call.message.chat.id, f'\nКатегория: {i.category.uz}, {pca}\nБошланғич нарх: {pna}\nМошина русуми: {i.avto.uz}, {i.kub} куб\nВилоят: {i.viloyat.uz}, {i.tuman.uz}\nТелефон рақам: {i.telefon}\nТелеграм: {una}\nТариф (пакет): {i.paket.name_uz}')
        btuz1 = types.InlineKeyboardMarkup()
        btuz1.add(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['next'], callback_data=f'search_{post_object.next_page_number()}'))
        bot.send_message(call.message.chat.id, f'({call.data.split("_")[1]} / {ceil(search_obj.count()/Service.get_count(Config.objects.all()))})', reply_markup=btuz1)
    else:
        from django.core.paginator import Paginator
        paginator = Paginator(search_obj, Service.get_count(Config.objects.all()))
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
            bot.send_message(call.message.chat.id, f'\nКатегория: {i.category.uz}, {pca}\nБошланғич нарх: {pna}\nМошина русуми: {i.avto.uz}, {i.kub} куб\nВилоят: {i.viloyat.uz}, {i.tuman.uz}\nТелефон рақам: {i.telefon}\nТелеграм: {una}\nТариф (пакет): {i.paket.name_uz}')
        btuz1 = types.InlineKeyboardMarkup()
        btuz1.row(types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['prev'], callback_data=f'search_{post_object.previous_page_number()}'), types.InlineKeyboardButton(text=LAN[Service.get_user_lan(TgUser.objects.filter(tg_id=call.message.chat.id))]['next_to'], callback_data=f'search_{post_object.next_page_number()}'))
        bot.send_message(call.message.chat.id, f'({call.data.split("_")[1]} / {ceil(search_obj.count()/Service.get_count(Config.objects.all()))})', reply_markup=btuz1)
