import telebot
from extensions import ConvertionException, Convertor
from config import TOKEN, money


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "Введите через пробел <имя валюты, цену которой хотите узнать>\n" \
           " <имя валюты, в которой надо узнать цену первой валюты>\n" \
           " <количество первой валюты!\n" \
           "/values - увидеть доступные валюты"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in money.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def get_price(message):
    try:
        values = message.text.split(' ')
        if len(values) > 3:
            raise ConvertionException('Слишком много параметров')
        if len(values) < 3:
            raise ConvertionException('Недостаточно данных')

        base, quote, amount = values
        total_base = Convertor.get_price(base, quote, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:
        text = f'Цена {amount} {base} в {quote}: {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True, interval=0)




