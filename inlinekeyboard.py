#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging
import os
import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update 
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes 

def Info(Names, Photo, Fact):
    person = {
        "name" : Names,
        'photo' : Photo,
        "fact": Factpy
    }
    return person

#def RandomFact(A):
    #fact1 = A.get('fact')
    #rand = random.randint(0,len(fact1)-1)
    #return(fact1[rand])

def grouped(array, num=3):
    array1 = [array[i:i+num] for i in range(0, len(array), num)]

#Данные о математиках и информатиках
Names = ["Алан Тьюринг", "Джон фон Нейман", "Эдсгер Вибе Дейкстра","Карл Фридрих Гаусс", "Софья Васильевна Ковалевская", "Пифагор", "Карл Вейерштрасс","Георг Кантор"]
Photo = ['/images/inform/1.jpg', '/images/inform/2.jpg', '/images/inform/3.jpg','/images/math/1.jpg','/images/math/2.jpg','/images/math/3.jpg','/images/math/4.jpg','/images/math/5.jpg']

Turing = ["Алан Мэтисон Тьюринг родился в Лондоне в 1912 году.", "В 1934 году он защитил диссертацию и стал профессором — ему в это время исполнилось всего 22 года.", "В годы Второй мировой Тьюринг и его команда взломали код Энигмы с помощью изобретения Тьюринга — электромеханической машины Bombe."]
Neumann = ["Джон фон Нейман hодился 28 декабря 1903 года.","В 1928 году Нейман написал статью «К теории стратегических игр»","Во время работ над созданием водородной бомбы фон Нейман и Станислав Улам разработали метод независимых статистических испытаний, известный теперь, как метод Монте-Карло."]
Dijkstra = ["Эдсгер Вибе Дейкстра, уроженец голландского Роттердама, появился на свет в 1930 году в семье ученых: отец был химиком, мать – математиком.", " Дейкстра не пользовался благами цивилизации, в его квартире не было телевизора и телефона, он не смотрел художественные фильмы.", "В 1972 году Дейкстра стал лауреатом премии Тьюринга."]
Gauss = ["Иоганн Карл Фридрих Гаусс — немецкий математик, механик, физик, астроном и геодезист. Считается одним из величайших математиков всех времён, «королём математики»", "Он открыл кольцо целых комплексных гауссовых чисел, создал для них теорию делимости.", "Гаусс в 62 года освоил русский, чтобы читать в оригинале труды Лобачевского."]
Kovalevskaya =["В возрасте 24 лет Софья Ковалевская получила звание доктора философии по математике, что было неслыханным достижением для юной дамы.", "Помимо математики, она увлекалась и литературой. Большинство её рассказов посвящены России, по которой она тосковала, находясь в другой стране.", "Софья Ковалевская умерла в возрасте 41 года, подхватив простуду во время поездки по Европе. Вернувшись в Стокгольм, где она в то время жила, она вскоре скончалась из-за воспаления лёгких."]
Pythagoras =["Пифагор, как известно, сделал огромный вклад в развитие геометрии. Однако, менее широко известен тот факт, что он преуспел и в ряде других наук.", "До наших дней не сохранилось ни одной письменной работы Пифагора.", "Впервые античные историки стали интересоваться жизнью Пифагора спустя примерно 2 века после его гибели."]
Weierstrass = ["Карл Вейерштасс родился 31 октября 1815 года в Остенфельде в семье чиновника.", "В 1854 году ученый публикует статью по абелевым функциям, за которую Кенигсбергский университет сразу присуждает ему степень доктора honoris causa (почетного доктора без защиты диссертации).", "В 1873 году Вейерштрасса избирают ректором Берлинского университета, а в 1881-м — членом Лондонского королевского общества."]
Cantor =["Георг Кантор  — немецкий математик, ученик Вейерштрасса.", "Георг был первенцем, старшим из шести детей. Он виртуозно играл на скрипке, унаследовав от своих родителей значительные художественные и музыкальные таланты.", "В 1870 г. Кантор доказал, что если функция непрерывна всюду на интервале, то её представление тригонометрическим рядом единственно."]

Fact = [Turing, Neumann, Dijkstra, Gauss, Kovalevskaya, Pythagoras, Weierstrass, Cantor]

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

def random_file(directory):
    files = os.listdir(directory)
    random_file = random.choice(files)
    return random_file


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Math", callback_data="1"),
            InlineKeyboardButton("Inform", callback_data="2"),
        ],
        [InlineKeyboardButton("Random", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    folder = ''

    if query.data == '1':
        folder = 'Math'
    elif query.data == '2':
        folder = 'Inform'
    else:
        folder = 'Math'

    image_name = random_file(f'images/{folder}')
    image_path = f'images/{folder}/{image_name}'
    
    await query.message.reply_photo(
        photo=open(image_path, 'rb')
    )

    await query.edit_message_text(text=f"Selected option: {query.data}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    TOKEN = '7136291430:AAFBxvDT2pGntZh3URfuCEdMInNU8W1i_oc'

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()