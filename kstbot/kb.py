from aiogram.filters import callback_data
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)


start = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Меню")]], resize_keyboard=True
)

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🌐 О нас", callback_data="about")],
        [InlineKeyboardButton(text="📚 Направления обучения", callback_data="sa")],
        [InlineKeyboardButton(text="❓ Основные вопросы", callback_data="faq")],
        [InlineKeyboardButton(text="🤝 Наши партнеры", callback_data="partners")],
        [InlineKeyboardButton(text="📨 Обратная связь", callback_data="feedback")],
    ]
)


faq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="❓Когда можно подать документы на обучение в колледж?",
                callback_data="faq_1",
            )
        ],
        [
            InlineKeyboardButton(
                text="❓Как подать документы на бюджет?", callback_data="faq_2"
            )
        ],
        [
            InlineKeyboardButton(
                text="❓Есть ли заочная форма обучения?",
                callback_data="faq_3",
            )
        ],
        [
            InlineKeyboardButton(
                text="❓Есть ли в колледже автошкола?",
                callback_data="faq_4",
            )
        ],
        [
            InlineKeyboardButton(
                text="❓Есть ли отсрочка от армии?", callback_data="faq_5"
            )
        ],
        [
            InlineKeyboardButton(
                text="❓Предоставляет колледж общежитие?", callback_data="faq_6"
            )
        ],
        [
            InlineKeyboardButton(
                text="❓Когда будет день открытых дверей?", callback_data="faq_7"
            )
        ],
        [InlineKeyboardButton(text="🔘Другое", callback_data="faq_other")],
        [InlineKeyboardButton(text="Назад", callback_data="menu")],
    ]
)

only_back = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="menu")]]
)

sa = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🏗️Строительство", callback_data="sa_1")],
        [InlineKeyboardButton(text="🏭Промышленность", callback_data="sa_2")],
        [InlineKeyboardButton(text="⚡️Энергетика", callback_data="sa_3")],
        [InlineKeyboardButton(text="🔧Транспорт", callback_data="sa_4")],
        [
            InlineKeyboardButton(
                text="👨‍💻Информационные технологии и безопасность", callback_data="sa_5"
            )
        ],
        [InlineKeyboardButton(text="📈Экономика", callback_data="sa_6")],
        [InlineKeyboardButton(text="Назад", callback_data="menu")],
    ]
)

partners = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🎓ВУЗы партнеры", callback_data="partners_1")],
        [InlineKeyboardButton(text="🤝Все партнеры", callback_data="partners_2")],
        [InlineKeyboardButton(text="Назад", callback_data="menu")],
    ]
)
