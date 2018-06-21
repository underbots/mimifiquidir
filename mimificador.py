# https://python-telegram-bot.org/
# Hili

from telegram.ext import Updater, CommandHandler
from config import TOKEN 

def mimificar(texto):
    vocales = "aeiou"
    
    for vocal in vocales:
        texto = texto.replace(vocal, 'i')
    
    return texto

def mimifica(bot, update):
    mimificado = mimificar(update.message.reply_to_message.text)
    update.message.reply_to_message.reply_text(mimificado)


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('mimifica', mimifica))

updater.start_polling()
updater.idle()
