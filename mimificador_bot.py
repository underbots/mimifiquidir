# https://python-telegram-bot.org/
# Hili, qui pisi

from telegram.ext import Updater, CommandHandler

from _config import TOKEN


def mimi(ms, indx=0):
    """ str -> str"""
    # caracteres especiales
    # que -> qui (la u no te la puede transformar )
    # gue -> gui (análogo al caso anterior)
    # c[aou] -> qui
    # g[aou] -> gui
    # estos casos han sido generados con un for de antemano

    esp = [['que', 'qui'], ['ca', 'qui'], ['co', 'qui'], ['cu', 'qui'],
           ['gue', 'gui'], ['ga', 'gui'], ['go', 'gui'], ['gu', 'gui'],
           ['QUE', 'QUI'], ['CA', 'QUI'], ['CO', 'QUI'], ['CU', 'QUI'],
           ['GUE', 'GUI'], ['GA', 'GUI'], ['GO', 'GUI'], ['GU', 'GUI']]
    i = 0

    while i < len(esp):
        ind = ms.find(esp[i][0])
        if ind != -1:
            return mimi(ms[0:ind], indx+1) + esp[i][1] + mimi(ms[ind+len(esp[i][0]):], indx)
        else:
            i += 1
    return mimi_normal(ms[0:])


def mimi_normal(ms):
    """ str -> stryt"""

    # Letras a reemplazar y su remplazamiento
    cadena = [["aeou", "i"], ["aeou".upper(), "I"], ["áéóú", "í"],
              ["áéóú".upper(), "I"]]

    for cad in cadena:
        for vocal in cad[0]:
            ms = ms.replace(vocal, cad[1])

    return ms


def mimifica(bot, update):
    mimificado = mimi(update.message.reply_to_message.text)
    update.message.reply_to_message.reply_text(mimificado)


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('mimifica', mimifica))
updater.dispatcher.add_handler(CommandHandler('mimi', mimifica))

updater.start_polling()
updater.idle()
