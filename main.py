import telebot
from telebot import types
from PIL import Image
def Run(bot):
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Привет ✌️ ")
    @bot.message_handler(commands=['button'])
    def button_message(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("индульгенция")
        markup.add(item1)
        #------------------------------------------------------------------------------
        item2 = types.KeyboardButton("Кнопка")
        markup.add(item2)
        bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

    @bot.message_handler(content_types='text')
    def message_reply(message):
        if message.text == "индульгенция":
            bot.send_photo(message.chat.id, Image.open("img\indulgence.jpg"))

def main():
    token = '6563307633:AAEEJG0xTAmpRUQfRKMxvPP25aNgtpNMZVk'
    bot = telebot.TeleBot(token)
    Run(bot)
    bot.infinity_polling()
if __name__ == '__main__':
    main()
