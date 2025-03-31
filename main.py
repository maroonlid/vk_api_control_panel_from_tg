import telebot
import bot_alphabet
import requests
from telebot import types

# для указание типов


def send_to_telegram(message):

    apiToken = '6512588978:AAE_M2JvYUXV8Av0ZOTEd08L804D_9gFhmo'
    chatID = '1215286915'
    chatID1 = '957045238'
    #chatID2 = '1058339360'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL , json={'chat_id': chatID, 'text': message})
        #response = requests.post(apiURL, json={'chat_id': chatID1, 'text': message})
        #response = requests.post(apiURL, json={'chat_id': chatID2, 'text': message})
        #print(response.text)
    except Exception as e:
        return




bot = telebot.TeleBot(bot_alphabet.apiToken)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Добавить новый аккаунт +")
    btn2 = types.KeyboardButton("Добавить новую группу рассылки +")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Этот бот создан для взаимодействия со спам-программой VK_elfbot. Используйте кнопки, чтобы продолжить.".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):

    if bot_alphabet.check1 == True and message.text != "Добавить новый аккаунт +" and message.text != "Добавить новую группу рассылки ➕":
        bot_alphabet.groups_id_list.append(message.text)
        bot.send_message(message.chat.id, text="<<Новая группа принята ✅>>")
        bot_alphabet.check1 = False

    elif bot_alphabet.check2 == True and message.text != "Добавить новый аккаунт +" and message.text != "Добавить новую группу рассылки +":

        bot_alphabet.list_number.append(message.text)
        bot_alphabet.check2 = False
        bot_alphabet.check3 = True
        bot.send_message(message.chat.id, text="Введите пароль -")

    elif bot_alphabet.check3 == True and message.text != "Добавить новый аккаунт +" and message.text != "Добавить новую группу рассылки +":
        bot_alphabet.list_password.append(message.text)
        bot_alphabet.write_in_file(bot_alphabet.list_number, bot_alphabet.list_password)
        bot.send_message(message.chat.id, text="<<Новый аккаунт принят ✅>>")
        #send_to_telegram("ACCOUNTS LEFT - " + str(len(bot_alphabet.list_number)))
        print(bot_alphabet.list_password)
        print(bot_alphabet.list_number)
        bot_alphabet.check3 = False

    elif (message.text == "Добавить новую группу рассылки +"):
        bot_alphabet.check1 = True
        bot.send_message(message.chat.id, text="Введите id -")
    elif (message.text == "Добавить новый аккаунт +"):
        bot.send_message(message.chat.id, text="Введите логин -")
        bot_alphabet.check2 = True

    elif (message.text == bot_alphabet.blocking_password):
        bot.send_message(message.chat.id, "<<ПРОГРАММА БЫЛА ОСТАНОВЛЕННА>>")
        exit(0)
    else:
        bot.send_message(message.chat.id, text="<неправильный запрос>")


bot.polling(none_stop=True)