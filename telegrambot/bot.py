import os
import telegram.ext
from telegram.ext import Updater, CommandHandler, MessageHandler
import datetime
import logging
import click
import cospiratoribot.commands as cc


@click.command()
@click.option("-v", count=True)
def main(v):
    verbosity = [
        logging.INFO,
        logging.DEBUG,
    ]
    logging.basicConfig(
        level=verbosity[min(v, 1)],
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


    token = os.environ["TOKEN"]
    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler('help', cc.help))
    updater.dispatcher.add_handler(CommandHandler('pilastri', cc.pilastri))
    updater.dispatcher.add_handler(CommandHandler('anni', cc.anni))
    updater.dispatcher.add_handler(CommandHandler('lenozzedifigaro', cc.lenozzedifigaro))
    updater.dispatcher.add_handler(CommandHandler('dongiovanni', cc.dongiovanni))
    updater.dispatcher.add_handler(CommandHandler('cosifantutte', cc.cosifantutte))
    updater.dispatcher.add_handler(CommandHandler('crocedoriente', cc.croce_oriente))
    updater.dispatcher.add_handler(CommandHandler('abulafia', cc.abulafia))
    updater.dispatcher.add_handler(CommandHandler('borges', cc.borges))
    updater.dispatcher.add_handler(CommandHandler('deutschland', cc.mozartlaugh))
    updater.dispatcher.add_handler(CommandHandler('dovesono', cc.dovesono))
    updater.dispatcher.add_handler(CommandHandler('dovesiamo', cc.dovesiamo))
    updater.dispatcher.add_handler(CommandHandler('oflgu210', cc.oflgu210))
    updater.dispatcher.add_handler(CommandHandler('mozart', cc.mozart))
    updater.dispatcher.add_handler(CommandHandler('15240100103043', cc.opera_solved))
    updater.dispatcher.add_handler(
        MessageHandler(
            ~telegram.ext.filters.Filters.location,
            cc.do_nothing))
    updater.dispatcher.add_handler(
        MessageHandler(
            telegram.ext.filters.Filters.location,
            cc.update_latest_positions))
    updater.start_polling(poll_interval=1)
    updater.idle()


if __name__ == "__main__":
    main()
