from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from parse.partners_parser import parse_partners


start = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Меню", callback_data="menu")]]
)

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="FAQ", callback_data="faq")],
        [InlineKeyboardButton(text="Обратная связь", callback_data="feedback")],
        [InlineKeyboardButton(text="Направления обучения", callback_data="sa")],
        [InlineKeyboardButton(text="О нас", callback_data="about")],
        [InlineKeyboardButton(text="Наши партнеры", callback_data="partners")],
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
                text="❓Есть ли отсрочка от армии?", callback_data="faq_3"
            )
        ],
        [
            InlineKeyboardButton(
                text="❓Есть ли вступительные испытания при поступлении?",
                callback_data="faq_4",
            )
        ],
        [
            InlineKeyboardButton(
                text="❓Как узнать проходной балл на специальность?",
                callback_data="faq_5",
            )
        ],
        [
            InlineKeyboardButton(
                text="❓Можно ли поступить в колледж после 10 класса?",
                callback_data="faq_6",
            )
        ],
        [
            InlineKeyboardButton(
                text="❓Предоставляет колледж общежитие?", callback_data="faq_7"
            )
        ],
        [
            InlineKeyboardButton(
                text="❓Когда будет день открытых дверей?", callback_data="faq_8"
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


def partners_inline_builder():
    partners_dict = parse_partners({}, "https://kstpro.ru/company/partners")

    partners_kb_builder = InlineKeyboardBuilder()
    for name, url in partners_dict.items():
        partners_kb_builder.add(InlineKeyboardButton(text=name, url=url))
    return InlineKeyboardMarkup(inline_keyboard=partners_kb_builder.export())
