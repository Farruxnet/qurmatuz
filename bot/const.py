USER_STEP = {
    'DEFAULT': 0,
    'LAN': 1,
    'EDIT_LAN': 3,
    'ADD_AVTO': 2,
    'GET_POD_CATEGORY': 4,
    'GET_KUB': 5,
    'GET_KUB_MANY': 6,
    'GET_VILOYAT': 7,
    'GET_POD_CAT': 8,
    'GET_TUMAN': 9,
    'GET_NARX': 10,
    'GET_TEL': 11,
    'GET_N': 12,
    'CHECK': 13,
    'FINAL': 14,
    'DONE' : 23,
    #### search ####
    'SEARCH': 15,
    'SEARCH_POD': 16,
    'SEARCH_AVTO': 17,
    'SEARCH_AVTO_KUB': 18,
    'SEARCH_VILOYAT': 19,
    'SEARCH_TUMAN': 20,
    'SEARCH_NARX': 21,
    'SEARCH_RESULT': 22
}

LAN = {
    'oz':{
        'delete': 'O\'chirish',
        'active': 'Faollashtirilgan',
        'act': 'Sizning hisobingizda mablag\' etarli emas! Hisobingizni mablag\' bilan to\'ldiring va \"Mening e\'lonlarim\" bo\'limida e\'loningizni faollashtiring. ',
        'balance_not': 'Hisobingizda mablag\' yetarli emas',
        'activ_ok': 'Faollashtirildi',
        'error': 'Xato! Qaytadan urunib ko\'ring.',
        'success_add': 'E\'lon qo\'shildi',
        'success_delete': 'E\'lon qabul qilinmadi',
        'done': 'Kiritgan ma\'lumotlaringiz to\'g\'rimi?',
        'yes': '✅ Ha to\'g\'ri',
        'no': '❌ Yo\'q noto\'g\'ri qaytadan yuboraman',
        'select': 'Tanlandi',
        'kelishilgan': '🤝 Kelishilgan narxda',
        'tel': '📞 Telefon raqam yuborish',
        'next': 'Keyingisi >',
        'next_to': 'Keyingi >',
        'prev': '< Oldingi',
        'homename': '🏠 Bosh sahifa',
        'homeback': '🏠 Bosh sahifa',
        'profile': "Profil",
        'back': 'Orqaga',
        'home': '🏠 Bosh sahifa',
        'settings': 'Profil',
        'search': '🔍 Qidirish',
        'addavto': '🚚 Moshina qo\'shish',
        'info': 'ℹ️ Ma\'lumot',
        'whouse': '❔ Qanday foydalaniladi?',
        'edit_lan': 'Tilni o\'zgartirish',
        'account_balance': 'Hisobni to\'ldirish',
        'about': 'Biz haqimizda',
        'contacts': 'Aloqa',
        'send_tel': 'Telefon raqamingizni yuboring.\nMisol: +998001234567 ko\'rinishida yoki pastdagi tugmani bosish orqali.',
        'start_price': 'Xizmatingiz boshlang\'ich narxi qancha?',
        'select_viloyat': 'Qaysi viloyat va tumanda xizmat ko\'rsatasiz? ',
        'service': 'Siz xizmat ko‘rsatadigan kategoriyani tanlang.',
        'service_pod': 'Siz xizmat ko‘rsatadigan kategoriyani tanlang. ',
        'select_avto': 'Avtomobilingiz rusumini tanlang',
        'select_avto_kub': 'Sizning avtomobilingiz qanday hajmda xizmat ko\'rsatadi? ',
        'select_plan': 'Tarif tanlang. Tariflar narxi va amal qilish muddati bilan farqlanadi.',
        'my_post': '📢 Mening e\'lonlarim',
        'post_not': 'Sizda e\'lonlar yo\'q',
        'balance': '💰 Hisobim',
        'activ': 'Faollashtirish',
        'search_what1': 'Qanday qurilish mahsuloti qidiryapsiz?',
        'search_pod1': 'Mahsulot turi qanday?',
        'search_avto1': 'Mahsulot uchun qanday mashina kerak?',
        'search_avto_kub1': 'Mashina hajmi qancha bo\'lsin?',
        'search_viloyat1': 'Qaysi viloyatdansiz?',
        'search_tuman1': 'Qaysi tumandansiz?',


    },

    'ru':{
        'delete': 'Удалить',
        'active': 'Активирован',
        'act': 'На вашем счету недостаточно денег! Пополните счет и активируйте свою рекламу в разделе «Мои объявления».',
        'balance_not': 'На вашем счету недостаточно денег',
        'activ_ok': 'Активирован',
        'next_to': 'Следующий >',
        'prev': '< Предыдущий',
        'error': 'Ошибка! Повторите попытку.',
        'success_add': 'Объявление добавлено',
        'success_delete': 'Объявление не было принято',
        'done': 'Правильная ли информация, которую вы ввели?',
        'yes': '✅ Да это правильно',
        'no': '❌ Нет неправильной повторной отправки',
        'select': 'выбранный',
        'kelishilgan': '🤝 По согласованной цене',
        'tel': '📞 Отправить номер телефона',
        'next': 'Следующий >',
        'homename': '🏠 Главная',
        'homeback': '🏠 Главная',
        'profile': "Profil",
        'back': 'Назад',
        'home': '🏠 Главная',
        'settings': 'Profil',
        'search': '🔍 Поиск',
        'addavto': '🚚 Добавить машину',
        'info': 'ℹ️ Информация',
        'whouse': '❔ Как пользоваться?',
        'edit_lan': 'Изменить язык',
        'account_balance': 'Пополнить счет',
        'about': 'О нас',
        'contacts': 'Обратная связь',
        'send_tel': 'Отправьте свой номер телефона.\nПример: в виде +998001234567 или нажав кнопку ниже.',
        'start_price': 'Какова начальная цена вашей услуги?',
        'select_viloyat': 'В какой провинции и районе вы обслуживаете?',
        'service': 'Выберите категорию, которую вы обслуживаете.',
        'service_pod': 'Выберите категорию, которую вы обслуживаете.',
        'select_avto': 'Выберите модель вашего авто',
        'select_avto_kub': 'Какая грузоподъемность вашего автомобиля?',
        'select_plan': 'Выберите тариф. Тарифы различаются по цене и сроку действия.',
        'my_post': '📢 Мои объявления',
        'post_not': 'У вас нет объявления',
        'balance': '💰 Мой счет',
        'activ': 'Активация',
        'search_what1': 'Какой строительный продукт вы ищете?',
        'search_pod1': 'Какой тип продукта?',
        'search_avto1': 'Какая машина вам нужна для продукта?',
        'search_avto_kub1': 'Какая вместимость машины?',
        'search_viloyat1': 'Из какой ты област?',
        'search_tuman1': 'Из какого ты района?',


    },

    'uz':{
        'delete': 'Ўчириш',
        'active': 'Фаоллаштирилган',
        'balance_not': 'Ҳисобингизда маблағ етарли эмас',
        'activ_ok': 'Фаоллаштирилди',
        'act': 'Сизнинг ҳисобингизда маблағ этарли эмас! Ҳисобингизни маблағ билан тўлдиринг ва "Менинг эълонларим" бўлимида эълонингизни фаоллаштиринг.',
        'next_to': 'Кейинги >',
        'prev': '< Олдинги',
        'error': 'Хато! Қайтадан уруниб кўринг.',
        'success_add': 'Эълон қўшилди',
        'success_delete': 'Эълон қабул қилинмади',
        'done': 'Киритган маълумотларингиз тўғрими?',
        'yes': '✅ Ха, тўғри',
        'no': '❌ Йўқ нотўғри қайтадан юбораман',
        'select': 'Танланди',
        'kelishilgan': '🤝 Келишилган нархда',
        'tel': '📞 Телефон рақам юбориш',
        'next': 'Кейингиси >',
        'homename': '🏠 Бош саҳифа',
        'homeback': '🏠 Бош саҳифа',
        'profile': "Profil",
        'back': 'Орқага',
        'home': '🏠 Бош саҳифа',
        'settings': 'Profil',
        'search': '🔍 Қидириш',
        'addavto': '🚚 Мошина қўшиш',
        'info': 'ℹ️ Маълумот',
        'whouse': '❔ Қандай фойдаланилади?',
        'edit_lan': 'Тилни ўзгартириш',
        'account_balance': 'Ҳисобни тўлдириш',
        'about': 'Биз ҳақимизда',
        'contacts': 'Aлоқа',
        'send_tel': 'Телефон рақамингизни юборинг.\nМисол: +998001234567 кўринишида ёки пастдаги тугмани босиш орқали.',
        'start_price': 'Хизматингиз бошланғич нархи қанча?',
        'select_viloyat': 'Қайси вилоят ва туманда хизмат кўрсатасиз? ',
        'service': 'Сиз хизмат кўрсатадиган категорияни танланг.',
        'service_pod': 'Сиз хизмат кўрсатадиган категорияни танланг.',
        'select_avto': 'Aвтомобилингиз русумини танланг',
        'select_avto_kub': 'Сизнинг автомобилингиз қандай ҳажмда хизмат кўрсатади? ',
        'select_plan': 'Тариф танланг. Тарифлар нархи ва амал қилиш муддати билан фарқланади.',
        'my_post': '📢 Менинг эълонларим',
        'post_not': 'Сизда эълонлар йўқ',
        'balance': '💰 Ҳисобим',
        'activ': 'Фаоллаштириш',
        'search_what1': 'Қандай қурилиш маҳсулоти қидиряпсиз?',
        'search_pod1': 'Маҳсулот тури қандай?',
        'search_avto1': 'Маҳсулот учун қандай машина керак?',
        'search_avto_kub1': 'Машина ҳажми қанча бўлсин?',
        'search_viloyat1': 'Қайси вилоятдансиз?',
        'search_tuman1': 'Қайси тумандансиз?',
    }
}
