import telebot
import wikipedia

bot = telebot.TeleBot('5434413208:AAHHjdlamJQGwUoVassTn9YJ_9TfmSZJFNI')

print(bot.get_me())


@bot.message_handler(commands=['wiki'])
def wiki(message):
    wikipedia.set_lang('ru')
    r = wikipedia.page(message.text.split(maxsplit=1)[1]).content

    if len(r) > 4096:
        for x in range(0, len(r), 4096):
            bot.send_message(message.chat.id, '{}'.format(r[x:x + 4096]))
            print(x)
    else:
        bot.send_message(message.chat.id, '{}'.format(r))


bot.infinity_polling(none_stop=True, interval=0)
