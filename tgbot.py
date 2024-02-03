from telebot import types
from datetime import datetime
import asyncio
from telebot.async_telebot import AsyncTeleBot
from telebot import asyncio_filters
from telebot.asyncio_storage import StateMemoryStorage
from telebot.asyncio_handler_backends import State, StatesGroup
from mytoken import token
import json
import codecs
from telebot.types import ReplyKeyboardRemove

with codecs.open("urls.json", 'r', "utf-8") as file:
    j = json.loads(file.read())

a1 = ''
b = 0
d = 0
x = 1
y = 0
q = 0
w = 0
p = 0
dictionary = set()

state_storage = StateMemoryStorage()
bot = AsyncTeleBot(token, state_storage=state_storage)

class botname(StatesGroup):
    name = State()

@bot.message_handler(commands = ["start"])   
async def cnt(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add("Поздороваться👋", "Задать вопрос❓")
    await bot.send_message(message.from_user.id, text = "Привет, {0.first_name}👋".format(message.from_user), reply_markup = markup)

@bot.message_handler(state = botname.name) 
async def cnt1(message):
    global a1
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text
    a1 = data['name']
    markupcnt2 = types.ReplyKeyboardMarkup(resize_keyboard= True)
    markupcnt2.add("Приступим🔼")
    await bot.send_message(message.chat.id, "Теперь меня зовут {name}".format(name = data['name']), parse_mode="html", reply_markup = markupcnt2)
    await bot.delete_state(message.from_user.id, message.chat.id)
    print("{0.first_name}".format(message.from_user), " назвал бота ", a1)

@bot.message_handler(content_types = ["text"])
async def cnt2(message): 
    global b, d, x, y, q, w, p, dictionary
    try:
        if (message.text == "Поздороваться👋"):
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup1.add("Приступим🔼", "Назад🔙")
            await bot.send_message(message.from_user.id, text = "И тебе привет, друг👋 Приступим к работе❓", reply_markup= markup1)
            print("{0.first_name}".format(message.from_user), "{0.last_name}".format(message.from_user), "{0.username}".format(message.from_user),"Поздоровался")

        elif (message.text == "Приступим🔼" or message.text == "Продолжить▶"):
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup2.add("Рассказать о праздниках🎈", "Выдать открытки🎫", "Уведомления⏰","Назад🔙")
            await bot.send_message(message.from_user.id, text = "Что мне сделать для тебя❓", reply_markup= markup2)

        elif (message.text == "Рассказать о праздниках🎈"):
            markup3 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup3.add(j[0]["name"][11], *j[0]["name"][0:11], "Другое🔙")
            await bot.send_message(message.from_user.id, text = "Окей, тогда выбирай месяц🌙", reply_markup = markup3)

        elif (message.text == "Выдать открытки🎫" or message.text == "Другое событие▶"):
            markup4 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup4.add(*j[13]["event"],"Другое🔙")
            await bot.send_message(message.from_user.id, text = "Выбирай событие🎈", reply_markup = markup4)

        elif (message.text in j[13]["event"]):
            events = j[13]["event"].index(message.text)
            day = j[13]["all_event"][events]
            markupev = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markupev.add("Другое событие▶")
            for i in range(len(j[13][day])):
                await bot.send_photo(message.chat.id, j[13][day][i])
            await bot.send_message(message.from_user.id, text = "Вот всё, что было🔎", reply_markup = markupev)

        elif (message.text == "Другое событие🔙"):
                markup4 = types.ReplyKeyboardMarkup(resize_keyboard = True)
                markup4.add(j[0]["name"][11], *j[0]["name"][0:11], "Другое🔙")
                await bot.send_message(message.from_user.id, text = "Выбирай событие🎈", reply_markup = markup4)

        elif (message.text == "Назад🔙"):
            markup5 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup5.add("Поздороваться👋", "Задать вопрос❓")
            await bot.send_message(message.from_user.id, text = "Вы вернулись назад🔙", reply_markup = markup5)

        elif (message.text == "Задать вопрос❓"):
            markup6 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup6.add("Как меня зовут❓", "Что я могу❓", "Назад🔙")
            await bot.send_message(message.from_user.id, text = "Задай мне вопрос❓", reply_markup = markup6) 

        elif (message.text == "Что я могу❓"):
            markup7 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup7.add("Приступим🔼", "Назад🔙")
            await bot.send_message(message.from_user.id, text = "Я могу рассказать тебе о ежедневных праздниках или выдать открытки🗓", reply_markup = markup7)

        elif (message.text == "Как меня зовут❓"):
            markup8 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup8.add("Хочу☺")
            await bot.send_message(message.from_user.id, text = "У меня нет имени, хочешь дать его мне❓", reply_markup = markup8)

        elif (message.text == "Хочу☺" and a1 == ''):   
            await bot.set_state(message.from_user.id, botname.name, message.chat.id)
            await bot.send_message(message.from_user.id, text = "Напиши, как меня будут звать🙃", reply_markup = ReplyKeyboardRemove())
            await bot.set_state(message.from_user.id, botname.name, message.chat.id)

        elif (message.text == "Хочу☺" and a1 != ''):
            markup9 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup9.add("Приступим🔼")
            await bot.send_message(message.from_user.id, text = "Ты мне уже дал имя❗ Меня зовут {name}".format(name = a1), parse_mode="html", reply_markup = markup9)
            
        elif (message.text == "Другое🔙"):
            markup10 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup10.add("Рассказать о праздниках🎈", "Выдать открытки🎫","Уведомления⏰", "Назад🔙")
            await bot.send_message(message.from_user.id, text = "Что мне сделать для тебя❓", reply_markup= markup10)

        elif (message.text == "Другой месяц🔙"):
            markup11 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup11.add(j[0]["name"][11], *j[0]["name"][0:11], "Другое🔙")
            await bot.send_message(message.from_user.id, text = "Не вопрос, выбери другой месяц🌙", reply_markup = markup11)
    
        elif (message.text == "Я ошибся("):
            markup12 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup12.add("Приступим🔼")
            await bot.send_message(message.from_user.id, text = "Окей, тогда давай приступим🔼", reply_markup = markup12)

        elif (message.text == "Уведомления⏰" and message.from_user.id not in dictionary):
            dictionary.add(message.from_user.id)
            markup14 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup14.add("Продолжить▶")
            await bot.send_message(message.from_user.id, text = "Теперь тебе будут приходить уведомления о праздниках", reply_markup = markup14)
            while message.from_user.id in dictionary:   
                await asyncio.sleep(1)
                now = datetime.now()   
                current_time = now.strftime("%H:%M:%S")
                if current_time == '00:00:00':
                    now = datetime.now()
                    day = now.strftime("%D")
                    day = list(day)
                    day.pop(2)
                    day.pop(4)
                    if current_time[0] == 0:
                        if current_time[2] == 0:
                            markup15 = types.ReplyKeyboardMarkup(resize_keyboard = True)
                            markup15.add("Приступим🔼")
                            await bot.send_message(message.from_user.id, text = "Сегодня " +  j[int(day[1])]["holiday"][int(day[3]) - 1] + " C Праздником!", reply_markup = markup15)
                            await asyncio.sleep(86390)
                        else:
                            markup15 = types.ReplyKeyboardMarkup(resize_keyboard = True)
                            markup15.add("Приступим🔼")
                            await bot.send_message(message.from_user.id, text = "Сегодня " +  j[int(day[1])]["holiday"][int(str(day[2]) + str(day[3])) - 1] + " C Праздником!", reply_markup = markup15)
                            await asyncio.sleep(86390)
                    else:
                        if current_time[2] == 0:
                            markup15 = types.ReplyKeyboardMarkup(resize_keyboard = True)
                            markup15.add("Приступим🔼")
                            await bot.send_message(message.from_user.id, text = "Сегодня " +  j[int(str(day[0]) + str(day[1])) - 1]["holiday"][int(day[3]) - 1] + " C Праздником!", reply_markup = markup15)
                            await asyncio.sleep(86390)
                        else:
                            markup15 = types.ReplyKeyboardMarkup(resize_keyboard = True)
                            markup15.add("Приступим🔼")
                            await bot.send_message(message.from_user.id, text = "Сегодня " +  j[int(str(day[0]) + str(day[1]))]["holiday"][int(str(day[2]) + str(day[3])) - 1] + " C Праздником!", reply_markup = markup15)
                            await asyncio.sleep(86390)

        elif (message.text == "Уведомления⏰" and message.from_user.id in dictionary):
            dictionary.discard(message.from_user.id)
            markup14 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup14.add("Продолжить▶")
            await bot.send_message(message.from_user.id, text = "Теперь тебе НЕ будут приходить уведомления о праздниках", reply_markup = markup14)
        
        elif (message.text in j[0]["name"]):
            days = []
            mt = message.text
            data = j[0]["name"].index(mt) 
            markupdays = types.ReplyKeyboardMarkup(resize_keyboard = True)
            for i in range(1, j[0]["days"][data] + 1):
                days.append((str(i) + " " + str(j[0]["second_name"][data])))
            markupdays.add(*days, "Другой месяц🔙")
            await bot.send_message(message.from_user.id, text = "Выбери число0️⃣", reply_markup = markupdays)

        elif (message.text in j[0]["pick_day"]):
            days = []
            mt = message.text
            pd = j[0]["pick_day"].index(mt)
            markupdays = types.ReplyKeyboardMarkup(resize_keyboard = True)
            for i in range(1, j[0]["days"][pd] + 1):
                days.append((str(i) + " " + str(j[0]["second_name"][pd])))
            markupdays.add(*days, "Другой месяц🔙")
            await bot.send_message(message.from_user.id, text = "Выбери число0️⃣", reply_markup = markupdays)
    
        elif (message.text.split()[1] in j[0]["second_name"]):
            sp = message.text.split()
            h = j[0]["second_name"].index(sp[1])
            markuphh = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markuphh.add(j[0]["pick_day"][h])
            await bot.send_message(message.from_user.id, text = j[h + 1]["holiday"][int(sp[0]) - 1], reply_markup = markuphh)
            await bot.send_photo(message.chat.id, j[h + 1]["url"][int(sp[0]) - 1])
    except:

        markupelse = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markupelse.add("Я ошибся(")
        await bot.send_message(message.from_user.id, text = "Я тебя не понимаю(", reply_markup = markupelse)

print("Online")
bot.add_custom_filter(asyncio_filters.StateFilter(bot))
bot.add_custom_filter(asyncio_filters.IsDigitFilter())
asyncio.run(bot.infinity_polling(timeout=90))