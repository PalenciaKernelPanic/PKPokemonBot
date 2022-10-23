import telegram
from telegram import Update, ParseMode
from telegram.ext import Updater, CallbackContext, CommandHandler, Defaults
from telegram.bot import Bot, BotCommand
import logging
import importlib

import config


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def tabla_tipos(update: Update, context: CallbackContext):
    update.message.reply_photo(photo='https://static.wikia.nocookie.net/pokemonreloaded/images/3/39/Efectividades.png/revision/latest/scale-to-width-down/680?cb=20141226072815&path-prefix=es')


def eficaz_contra(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        msg = 'Tienes que especificar un tipo'
    elif not is_ascii(context.args[0]):
        msg = 'Escribe el tipo sin tildes'
    else:
        class_name = context.args[0].capitalize()
        MiTipo = getattr(importlib.import_module('tablatipos.tipos'), class_name)
        t = MiTipo()
        msg = f'El tipo *{class_name}* es __eficaz contra__: _{t.get_eficaz_contra()}_'
    update.message.reply_text(text=msg)


def poco_eficaz_contra(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        msg = 'Tienes que especificar un tipo'
    elif not is_ascii(context.args[0]):
        msg = 'Escribe el tipo sin tildes'
    else:
        class_name = context.args[0].capitalize()
        MiTipo = getattr(importlib.import_module('tablatipos.tipos'), class_name)
        t = MiTipo()
        msg = f'El tipo *{class_name}* es __poco eficaz contra__: _{t.get_poco_eficaz_contra()}_'
    update.message.reply_text(text=msg)


def resistente_ante(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        msg = 'Tienes que especificar un tipo'
    elif not is_ascii(context.args[0]):
        msg = 'Escribe el tipo sin tildes'
    else:
        class_name = context.args[0].capitalize()
        MiTipo = getattr(importlib.import_module('tablatipos.tipos'), class_name)
        t = MiTipo()
        msg = f'El tipo *{class_name}* es __resistente ante__: _{t.get_resistente_ante()}_'
    update.message.reply_text(text=msg)


def debil_ante(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        msg = 'Tienes que especificar un tipo'
    elif not is_ascii(context.args[0]):
        msg = 'Escribe el tipo sin tildes'
    else:
        class_name = context.args[0].capitalize()
        MiTipo = getattr(importlib.import_module('tablatipos.tipos'), class_name)
        t = MiTipo()
        msg = f'El tipo *{class_name}* es __debil ante__: _{t.get_debil_ante()}_'
    update.message.reply_text(text=msg)


def stats(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        msg = 'Tienes que especificar un tipo'
    elif not is_ascii(context.args[0]):
        msg = 'Escribe el tipo sin tildes'
    else:
        class_name = context.args[0].capitalize()
        MiTipo = getattr(importlib.import_module('tablatipos.tipos'), class_name)
        t = MiTipo()
        msg = f'''El tipo *{class_name}* es:
        \- eficaz contra: _{t.get_eficaz_contra()}_
        \- poco eficaz contra: _{t.get_poco_eficaz_contra()}_
        \- resistente ante: _{t.get_resistente_ante()}_
        \- debil ante: _{t.get_debil_ante()}_'''
    update.message.reply_text(text=msg)


def help(update: Update, context: CallbackContext):
    msg = """
/help: Muestra un mensaje de ayuda
/tabla\_tipos: Muestra la tabla de tipos
/stats _\<tipo\>_: Muestra eficacia, resistencia y debilidad contra otros tipos
/eficaz\_contra _\<tipo\>_: Tipos contra los que es eficaz
/poco\_eficaz\_contra _\<tipo\>_: Tipos contra los que es poco eficaz
/resistente\_ante _\<tipo\>_: Tipos antes los que es resistente
/debil\_ante _\<tipo\>_: Tipos ante los que es débil
    """
    update.message.reply_text(text=msg)


def main():
    defaults = Defaults(parse_mode=ParseMode.MARKDOWN_V2)

    # Bot Commands
    commands = [
        BotCommand("help", "Muestra un mensaje de ayuda"),
        BotCommand("tabla_tipos", "Muestra la tabla de tipos"),
        BotCommand("stats", "Muestra eficacia, resistencia y debilidad contra otros tipos"),
        BotCommand("eficaz_contra", "Tipos contra los que es eficaz"),
        BotCommand("poco_eficaz_contra", "Tipos contra los que es poco eficaz"),
        BotCommand("resistente_ante", "Tipos antes los que es resistente"),
        BotCommand("debil_ante", "Tipos ante los que es débil"),
    ]
    bot = Bot(token=config.TOKEN)
    bot.set_my_commands(commands)  # this is to show the available commands

    updater = Updater(token=config.TOKEN, defaults=defaults)
    dispatcher = updater.dispatcher

    # Command handlers
    help_handler = CommandHandler('help', help)
    tabla_tipos_handler = CommandHandler('tabla_tipos', tabla_tipos)
    stats_handler = CommandHandler('stats', stats)
    eficaz_contra_handler = CommandHandler('eficaz_contra', eficaz_contra)
    poco_eficaz_contra_handler = CommandHandler('poco_eficaz_contra', poco_eficaz_contra)
    resistente_ante_handler = CommandHandler('resistente_ante', resistente_ante)
    debil_ante_handler = CommandHandler('debil_ante', debil_ante)

    # Adding handlers to the dispatcher
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(tabla_tipos_handler)
    dispatcher.add_handler(stats_handler)
    dispatcher.add_handler(eficaz_contra_handler)
    dispatcher.add_handler(poco_eficaz_contra_handler)
    dispatcher.add_handler(resistente_ante_handler)
    dispatcher.add_handler(debil_ante_handler)


    # Starts to listen
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
