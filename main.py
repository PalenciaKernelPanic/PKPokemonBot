from typing import Any, Tuple, Union, List

from telegram import Update, ParseMode
from telegram.ext import Updater, CallbackContext, CommandHandler, Defaults, DispatcherHandlerStop, TypeHandler
from telegram.bot import Bot, BotCommand
import logging
import importlib

import config
from _version import __version__

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def is_ascii(s):
    """
        Comprueba que no se han introducido tildes.
    """
    return all(ord(c) < 128 for c in s)


def check_args(args: Union[List['str']]) -> Tuple[bool, str, str, Union[bool, Any]]:
    """
        Comprueba que los argumentos pasados no llevan tilde, estan presentes y devuelve un objeto del tipo instanciado.
    """
    ok = t = False
    if isinstance(args, list) and len(args) == 1:
        return ok, '', 'Tienes que especificar un tipo', t
    elif not is_ascii(args[1]):
        return ok, '', 'Escribe el tipo sin tildes', t
    else:
        ok = True
        class_name = args[1].capitalize()
        MiTipo = getattr(importlib.import_module('tablatipos.tipos'), class_name)
        t = MiTipo()
        return ok, class_name, '', t


def tabla_tipos(update: Update, context: CallbackContext):
    """
        Devuelve una imagen con la tabla de tipos
    """
    update.message.reply_photo(
        photo='https://static.wikia.nocookie.net/pokemonreloaded/images/3/39/Efectividades.png/revision/latest/scale-to-width-down/680?cb=20141226072815&path-prefix=es')


def help(update: Update, context: CallbackContext):
    """
        Mensaje de ayuda con los comandos y sus descripciones.
    """
    msg = f"""v{__version__}
/help: Muestra un mensaje de ayuda
/tabla\_tipos: Muestra la tabla de tipos
/stats _<tipo>_: Muestra eficacia, resistencia y debilidad contra otros tipos
/eficaz\_contra _<tipo>_: Tipos contra los que es eficaz
/poco\_eficaz\_contra _<tipo>_: Tipos contra los que es poco eficaz
/resistente\_ante _<tipo>_: Tipos antes los que es resistente
/debil\_ante _<tipo>_: Tipos ante los que es débil
    """.replace('.', '\\.').replace('<', '\\<').replace('>', '\\>')
    update.message.reply_text(text=msg)


def generic_cmd(cmd: str, args: List[str]) -> str:
    """
        Para ejecutar cualquiera de los 5 comandos de estadísticas de tipos.
    """
    ok, tipo, msg, t = check_args(args)
    if ok:
        if cmd != 'stats':
            msg = f"El tipo *{tipo}* es __{' '.join(cmd.split('_'))}__: _{eval('t.get_' + cmd + '()')}_"
        else:
            msg = f'''El tipo *{tipo}* es:
\- eficaz contra: _{t.get_eficaz_contra()}_
\- poco eficaz contra: _{t.get_poco_eficaz_contra()}_
\- resistente ante: _{t.get_resistente_ante()}_
\- debil ante: _{t.get_debil_ante()}_'''
    return msg


def callback(update: Update, context: CallbackContext):
    """
        Para manejar los 5 comandos de estadisticas de tipos.
    """
    cmd_not_to_handle = ['stats', 'eficaz_contra', 'poco_eficaz_contra', 'resistente_ante', 'debil_ante']
    cmd = update.effective_message.text.split()[0].lstrip('/')
    logging.info(f'{update.effective_message.from_user.username}: {update.effective_message.text}')
    if cmd in cmd_not_to_handle:
        msg = generic_cmd(cmd, update.effective_message.text.split())
        update.message.reply_text(text=msg)
        raise DispatcherHandlerStop  # do not handle this command


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
    generic_handler = TypeHandler(Update, callback)
    help_handler = CommandHandler('help', help)
    tabla_tipos_handler = CommandHandler('tabla_tipos', tabla_tipos)

    # Adding handlers to the dispatcher
    dispatcher.add_handler(generic_handler, -1)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(tabla_tipos_handler)

    # Starts to listen
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
