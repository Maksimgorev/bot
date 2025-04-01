#импортировал библеотеку
import telebot
from sys import *
from datetime import datetime
import per


bot =telebot.TeleBot ('')




current_time = datetime.now()
target_time = datetime(year=2025,month= 4,day = 1,hour=0,minute=0)
message_1 = "Пора избавится от задолжностей"

#name = None

#def user_name(message):
#    global name
 #   name = message.text.strip()
  #  bot.send_message(message.chat.id,"Введите пароль:")
   # bot.register_next_step_handler(message,user_pass)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'''Вы попали в чат-бот Омутнинского политехнического техникума.
Что же вас интересует?
На какие профессии обучают в нашем учебном заведении?
Сроки обучения?
Когда собеседование?
Какие документы нужно принести для поступления?
На все эти вопросы вы найдёте ответ в данном боте.''', reply_markup = per.markup)
#   conn = sqlite3.connect('проект\боты\пользователь.db')
  #  cur = conn.cursor()
   # cur.execute('''CREATE TABLE IF NOT EXISTS products(
    #    id INTEGER PRIMARY KEY AUTOINCREMENT,
     #   name TEXT,
      #  Password TEXT
    #);''')
    #conn.commit()
    #cur.close()
    #conn.close()
    #bot.send_message(message.chat.id,"Напишите свое имя")
   # bot.register_next_step_handler(message,user_name)


#def user_pass(message):
 #   password = message.text.strip()
   # conn = sqlite3.connect('проект\боты\пользователь.db')
  #  cur = conn.cursor()
    #cur.execute("INSERT INTO users(name,pass) VALUES('%s'),('%s')"(name,password))
 #   conn.commit()
  #  cur.close()
   # conn.close()
    #bot.send_message(message.chat.id,"Спасибо, ты зарегистрирован",per.text,reply_markup = per.markup)


@bot.message_handler(content_types=['text']) 
def knopks(message):
    if message.chat.type == "private":
        if message.text == "Социальные сети":
            bot.send_message(message.chat.id,"Какие вам социальные сети нужны у Омутнинского политехнического техникума, нажмите на нижнюю кнопку",
            reply_markup=per.knopka)


        elif message.text == "Договоры":
            bot.send_message(message.chat.id,"Лучше узнать это у Надежды Васильевны",reply_markup=per.key_2)


        elif message.text == "приёмная":
            bot.send_message(message.chat.id,'+7(83352)2-23-53')


        elif message.text == 'учителя':
            bot.send_message(message.chat.id,per.text_2, parse_mode = 'html')


































        elif message.text == 'документы':
            bot.send_message(message.chat.id,per.text_3,parse_mode = 'html')       


        elif message.text == 'профессии':
            bot.send_message(message.chat.id,'''
        <b>КОГПОАУ "Омутнинский политехнический техникум"</b> объявляет приём на <u>2025 - 2026</u> учебный год на обучение по профессиям:
    на базе общего основного образования
                ''', parse_mode= 'html')
            bot.send_message(message.chat.id,per.text_4, parse_mode = 'html')


        elif message.text == "Электронный дневник":
            bot.send_message(message.chat.id,per.text_5,reply_markup= per.knopka_3)

        
        elif message.text == "Стипендия":
            bot.send_message(message.chat.id, "что бы вы хотели бы узнать?",reply_markup = per.knopka_4)
            if message.text == "Сколько осталось до стипендии":
                    days_left = (target_time - current_time).days
                    if days_left > 0:
                        bot.send_message(message.chat.id, f'До стипендии осталось {days_left} дней.')
                    elif days_left == 0:
                        bot.send_message(message.chat.id, 'Сегодня день стипендии!')
            elif message.text == "Время до стипендии":
                if current_time == target_time:
                    bot.send_message(message.chat.id,"время пришло")
                elif current_time < target_time:
                    bot.send_message(message.chat.id,"Время еще не пришло")
                elif current_time > target_time:
                    bot.send_message(message.chat.id,"Вы опаздали")
            elif message.text == "За что платят стипендию?":
                bot.send_message(message.chat.id,per.text_6)















        elif message.text == "фотография учителей":
            bot.send_photo(message.chat.id,url = "indev_project/боты/bot_photo/учителя.jpg")


















if current_time == target_time:
    def check_current_time(message):
        bot.send_message(message.chat.id,message_1)




    


        #elif message.text == "Расписание":
        #    bot.message_handler(message.chat.id,"расписание с 17 по 21")
        #    bot.send_photo(message.chat.id, open(per.photo,"r"))

#@bot.message_handler(content_types=['Сз'])
#def spisok_reg(): 

bot.polling(none_stop=True)



#реализация у друга идеи
