# -*- coding: utf-8 -*-
import telebot
from telebot.formatting import hbold, format_text
from telebot import types
bot = telebot.TeleBot('')


def create_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item_menu = types.KeyboardButton('Меню')
    markup.add(item_menu)
    return markup


def create_menu_buttons():
    markup_menu = types.InlineKeyboardMarkup(row_width=1)
    item_about_kst = types.InlineKeyboardButton('🌐 О нас', callback_data='about_kst')
    item_areas_of_study = types.InlineKeyboardButton('📚 Направления обучения', callback_data='areas_of_study')
    item_faq = types.InlineKeyboardButton('❓ Основные вопросы', callback_data='main_questions')
    item_partners = types.InlineKeyboardButton('🤝🏼 Наши партнеры', callback_data='partners_kst')
    item_feedback = types.InlineKeyboardButton('📨 Обратная связь', callback_data='feedback')
    item_refresh = types.InlineKeyboardButton('🔄 Обновить бота', callback_data='refresh_bot')
    markup_menu.add(item_about_kst, item_areas_of_study, item_faq, item_partners, item_feedback, item_refresh)
    return markup_menu


def create_faq_buttons():
    markup_faq = types.InlineKeyboardMarkup(row_width=1)
    questions = [
        '❓ Когда можно подать документы на обучение в колледж?',
        '❔ Как подать документы на бюджет?',
        '❓ Есть ли заочная форма обучения?',
        '❔ Есть ли в колледже автошкола?',
        '❓ Есть ли отсрочка от армии?',
        '❔ Предоставляет колледж общежитие?',
        '❓ Когда будет день открытых дверей?',
        '🔘 Другое'
    ]
    for i, question_text in enumerate(questions, start=1):
        question_button = types.InlineKeyboardButton(f'{question_text}', callback_data=f'q{i}')
        markup_faq.add(question_button)
    back_button = types.InlineKeyboardButton('Назад', callback_data='back_to_menu')
    markup_faq.add(back_button)
    return markup_faq

def create_partners_kst_buttons():
    markup_partners = types.InlineKeyboardMarkup(row_width=1)
    partners = [
        '🎓ВУЗы партнеры',
        '🤝🏼Все партнеры',
    ]
    for i, partner_text in enumerate(partners, start=1):
        partner_button = types.InlineKeyboardButton(f'{partner_text}', callback_data=f'partner{i}')
        markup_partners.add(partner_button)
    back_button = types.InlineKeyboardButton('Назад', callback_data='back_to_menu')
    markup_partners.add(back_button)
    return markup_partners

def about_kst_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    about_kst_text = format_text(hbold("ГБПОУ КСТ"),
                               "🎓 - Колледж Современных Технологий имени Героя Советского Союза М.Ф. Панова является образовательным учреждением, которое подготавливает квалифицированных специалистов.\n\n"
                               "🔧 - Учебное заведение акцентирует внимание на практических навыках и умениях для успешной карьеры.\n\n"
                               "🏫 - В колледже есть современные учебные классы и лаборатории, что способствует качественному обучению студентов.\n\n"
                               "👩‍🏫 - Преподаватели колледжа отличаются высокой квалификацией и доброжелательностью.\n\n"
                               "🕒 - Режим работы колледжа организован таким образом, чтобы обеспечить удобство и доступность обучения для всех участников учебного процесса.\n\n"
                               "📈 - Учреждение постоянно стремится к улучшению качества предоставляемых образовательных услуг и внимательно относится к отзывам студентов.")

    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=about_kst_text, reply_markup=create_menu_buttons(), parse_mode="HTML")

def create_study_buttons():
    markup_study = types.InlineKeyboardMarkup(row_width=1)
    study_options = [
        '🏗️ Строительство',
        '🏭 Промышленность и инженерные технологии',
        '⚡ Энергетика',
        '🔧 Транспорт',
        '👨‍💻 Информационные технологии и безопасность',
        '📉 Экономика'
    ]
    for i, study_text in enumerate(study_options, start=1):
        study_button = types.InlineKeyboardButton(f'{study_text}', callback_data=f'study{i}')
        markup_study.add(study_button)
    back_button = types.InlineKeyboardButton('Назад', callback_data='back_to_menu')
    markup_study.add(back_button)
    return markup_study


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=create_main_menu())


@bot.message_handler(func=lambda message: message.text == 'Меню')
def menu_handler(message):
    bot.send_message(message.chat.id, "Меню:", reply_markup=create_menu_buttons())


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    if call.data == 'refresh_bot':
        new_text = "Бот обновлен!"
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=new_text)

    elif call.data == 'main_questions':
        faq_text = "Выберите вопрос"
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=faq_text, reply_markup=create_faq_buttons())

    elif call.data.startswith('q'):
        question_num = call.data[1:]
        response_dict = {
            '1': ('❓Когда можно подать документы на обучение в колледж?', '✅Сроки приема на бюджетные места : с 20 июня по 15 августа!'),
            '2': ('❓Как подать документы на бюджет?', '✅Сначала нужно зарегистрироваться на портале mos.ru.'
                                                      '\n-Из личного кабинета абитуриента в период с 20 июня по 15 августа подать заявление.'
                                                      '\n-Прикрепить сканы паспорта (первая страница и регистрация) и аттестата с приложением.'
                                                      '\n-После получения уведомления о том, что вы рекомендованы к зачислению, необходимо прийти в приемную комиссию КСТ с оригиналом аттестата в течение 5 дней.'
                                                      '\n-Несовершеннолетнему абитуриенту необходимо прийти в сопровождении родителя (законного представителя)!'),
            '3': ('❓Есть ли заочная форма обучения?', '✅Да, есть!\nПрием документов с 1 июня по 25 декабря текущего года.'),
            '4': ('❓Есть ли в колледже автошкола?', '✅Да, есть! \nНаш колледж предоставляет услуги по обучению на рзличные категории вождения.\nУзнайте подробнее на [сайте колледжа](kstpro.ru/product/avtoshkola/).'),
            '5': ('❓Есть ли отсрочка от армии?', '✅Да! На весь период обучения!'),
            '6': ('❓Предоставляет колледж общежитие?', '✅Нет, общежитие не предоставляется.'),
            '7': ('❓Когда будет день открытых дверей?', '✅Единый день открытых дверей состоится 12 марта в 11:00 по адресу: Хибинский проезд, дом 10!'
                                                        '\n❗Регистрируйтесь на мероприятие по [ссылке](kstpro.ru/events/den-otkrytykh-dverey/edinyy-..)!'),
            '8': ('🔘Другое', '❗Если у тебя остались вопросы - звони в приемную комиссию по телефонам:'
                  '\n✅8-499-188-08-83\n✅8-966-379-85-23')
        }
        faq_text, response = response_dict.get(question_num, (
            "Извините, ответ на этот вопрос пока недоступен.", "Извините, ответ на этот вопрос пока недоступен."))

        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'{faq_text}\n\n{response}',
                              parse_mode='Markdown', reply_markup=create_faq_buttons())

    elif call.data == 'back_to_menu':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Меню:", reply_markup=create_menu_buttons())

    elif call.data == 'feedback':
        feedback_info = "📨 Обратная связь\n\n" \
                        "Телефон: \n✅8-499-188-08-83\n✅8-966-379-85-23\n" \
                        "Email: kst@edu.mos.ru\n" \
                        "Адрес: [Москва, Хибинский проезд, 10](https://yandex.ru/maps/-/CDqEvUln)\n" \
                        "Сайт колледжа: [kstpro.ru](https://kstpro.ru)"

        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=feedback_info,
                              parse_mode='Markdown', reply_markup=create_menu_buttons())

    elif call.data == 'areas_of_study':
        study_text = "Направления подготовки в ГБПОУ КСТ"
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=study_text, reply_markup=create_study_buttons())

    elif call.data.startswith('study'):
        study_num = call.data[5:]
        response_dict = {
            '1': ('🏗 Строительство', 'Для получения актуальной информации по направлению "[Строительство](kstpro.ru/spetsialnosti/stroitelstvo/)", посетите сайт колледжа и выберите понравившуюся специализацию.'),
            '2': ('🏭 Промышленность и инженерные технологии', 'Для получения актуальной информации по направлению "[Промышленность и инженерные технологии](kstpro.ru/spetsialnosti/promyshlennye-i-inzhenernye-tehnologii/)", посетите сайт колледжа и выберите понравившуюся специализацию.'),
            '3': ('⚡ Энергетика', 'Для получения актуальной информации по направлению "[Энергетика](kstpro.ru/spetsialnosti/energetika/)", посетите сайт колледжа и выберите понравившуюся специализацию.'),
            '4': ('🔧 Транспорт', 'Для получения актуальной информации по направлению "[Транспорт](kstpro.ru/spetsialnosti/transport/)", посетите сайт колледжа и выберите понравившуюся специализацию.'),
            '5': ('👨‍💻 Информационные технологии и безопасность', 'Для получения актуальной информации по направлению "[Информационные технологии и безопасность](kstpro.ru/spetsialnosti/informatsionnye-tehnologii-i-bezopasnost/)", посетите сайт колледжа и выберите понравившуюся специализацию.'),
            '6': ('📈 Экономика', 'Для получения актуальной информации по направлению "[Экономика](kstpro.ru/spetsialnosti/ekonomika/)", посетите сайт колледжа и выберите понравившуюся специализацию.')
        }
        study_question, study_response = response_dict.get(study_num, (
            "Извините, информация по этому направлению пока недоступна.", "Извините, информация по этому направлению пока недоступна."))

        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'{study_question}\n\n{study_response}',
                              parse_mode="Markdown", reply_markup=create_study_buttons())
    elif call.data == 'partners_kst':
        partners_text = "Наши партнеры"
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=partners_text,
                              reply_markup=create_partners_kst_buttons())

    elif call.data.startswith('partner'):
        partner_num = call.data[7:]
        response_dict = {
            '1': ('🎓[ВУЗы партнеры](kstpro.ru/company/partners/)', '▫Московский политехнический университет\n▫Московский автомобильно-дорожный государственный технический университет (МАДИ)\n▫Национальный исследовательский университет «МЭИ» (Московский энергетический институт)\n▫НИУ МГСУ — Московский строительный университет\n▫Московский технический университет связи и информатики (МТУСИ)\n▫Российский университет дружбы народов (РУДН)'),
            '2': ('🤝🏼Все партнеры', 'Для получения актуальной информации по всем партнерам КСТ, перейдите на [сайт колледжа](kstpro.ru/company/partners/)')
        }
        partner_name, partner_info = response_dict.get(partner_num, (
            "Извините, информация о этом партнере пока недоступна.",
            "Извините, информация о этом партнере пока недоступна."))

        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'{partner_name}\n\n{partner_info}',
                              parse_mode='Markdown', reply_markup=create_partners_kst_buttons())

    elif call.data == 'about_kst':
        about_kst_handler(call)

bot.infinity_polling()
