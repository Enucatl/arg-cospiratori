import os
import numpy as np
import telegram.ext
from telegram.ext import Updater, CommandHandler, MessageHandler
import logging
import datetime


ids = {
    "Matteo": 62030274,
    "Massimo": 82200874,
    "Alessio": 127145721,
    "Stefano": 45006035,
    "Roberto": 85010254,
    "Daniele": 85218517,
}

targets = {
    82200874: {
        "lat": 52.503192,
        "lon": 13.444954
    },
    127145721: {
        "lat": 48.581551,
        "lon": 7.750155
    },
    45006035: {
        "lat": 46.509946,
        "lon": 6.556047
    },
    85010254: {
        "lat": 47.535275,
        "lon": 8.221467
    },
    85218517: {
        "lat": 45.707831,
        "lon": 9.410977
    },
}

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def help(bot, update):
    update.message.reply_text(
        """
c'è una cosa che è successa a cui dovete rimediare...
chi è??? NOOOO... FERMI COSA FATE!!!!! ahhhhh!



Siete stati scoperti, avete dieci giorni per riattivare
i sacri pilastri... altrimenti verremo a prendere
anche voi HAHAHAHAHAHAHAHAHA!
        """)


def pilastri(bot, update):
    update.message.reply_text(
        text="""
*Fu antico test*
Vi do inganno:
delfini, gazze, oro
        """,
        parse_mode=telegram.ParseMode.MARKDOWN,
        quote=False)
    update.message.reply_text(
        text="/anni 🇮🇹 🇫🇷 ***",
        quote=False)


def lenozzedifigaro(bot, update):
    update.message.reply_text(
        text="5 * 20 * 36 *")


def dongiovanni(bot, update):
    update.message.reply_text(
        text="91 100 231 640 1003")


def cosifantutte(bot, update):
    update.message.reply_text(
        text="anni 1 100 1000")


def opera_solved(bot, update):
    update.message.reply_text(
        """
OFLGU210
        """
    )


def anni(bot, update):
    update.message.reply_photo(
        open("abulafia.png", "rb"),
        quote=False
    )


def croce_oriente(bot, update):
    update.message.reply_text(
        """
dove sei?
portami ai piedi
della croce d'oriente
        """
    )
    

def distance(lat1, lon1, lat2, lon2):
    r = 6371
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = phi2 - phi1
    delta_lambda = np.radians(lon2 - lon1)
    a = (np.sin(delta_phi/2) * np.sin(delta_phi/2) +
        np.cos(phi1) * np.cos(phi2) *
        np.sin(delta_lambda/2) * np.sin(delta_lambda/2))
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return r * c


def dovesono(bot, update):
    check_positions_in_last_hour()
    if (update.message.from_user.id == ids["Matteo"]
        and ids["Matteo"] in position_dictionary):
        ostkreuz = {
            "lat": 52.503267,
            "lon": 13.469323
        }
        d = distance(
            position_dictionary[ids["Matteo"]]["lat"],
            position_dictionary[ids["Matteo"]]["lon"],
            ostkreuz["lat"],
            ostkreuz["lon"])
        update.message.reply_text(
            "{%.1f} km".format(d),
            quote=False)
        if d < 0.2:
            update.message.reply_photo(
                open("pillars-1200x480.jpg.1", "rb"),
                quote=False)
    else:
        update.message.reply_text(
            "Impossibile rintracciare l'agente {}".format(ids["Matteo"]))


def dovesiamo(bot, update):
    check_positions_in_last_hour()
    total_distance = 0
    for target in targets:
        if not target in position_dictionary:
            update.message.reply_text(
                "Impossibile rintracciare l'agente {}".format(target))
            return
        else:
            total_distance += distance(
                position_dictionary[target]["lat"],
                position_dictionary[target]["lon"],
                targets[target]["lat"],
                targets[target]["lon"])
    update.message.reply_text(
        "{%.1f} km".format(total_distance),
        quote=False)
    if total_distance < 0.5:
        update.message.reply_text(
            "https://www.youtube.com/watch?v=04854XqcfCY",
            quote=False)


def forward(bot, update):
    if update.message.chat.id > 0:
        chat_name = update.message.chat.first_name
    else:
        chat_name = update.message.chat.title
    bot.send_message(
        chat_id=62030274,
        text="{} ({}): {}".format(
            update.message.from_user.first_name,
            chat_name,
            update.message.text))


position_dictionary = {}
def update_latest_positions(bot, update):
    lat = update.message.location.latitude
    lon = update.message.location.longitude
    from_id = update.message.from_user.id
    timestamp = update.message.date
    position_dictionary[from_id] = {
        "timestamp": timestamp,
        "lat": lat,
        "lon": lon,
    }
    check_positions_in_last_hour()

def check_positions_in_last_hour():
    for key, value in position_dictionary.items():
        if (value["timestamp"] - datetime.datetime.now()).total_seconds() > 3600:
            del position_dictionary[key]


token = os.environ["TOKEN"]
updater = Updater(token)
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('pilastri', pilastri))
updater.dispatcher.add_handler(CommandHandler('anni', anni))
updater.dispatcher.add_handler(CommandHandler('lenozzedifigaro', lenozzedifigaro))
updater.dispatcher.add_handler(CommandHandler('dongiovanni', dongiovanni))
updater.dispatcher.add_handler(CommandHandler('cosifantutte', cosifantutte))
updater.dispatcher.add_handler(CommandHandler('crocedoriente', croce_oriente))
updater.dispatcher.add_handler(CommandHandler('dovesono', dovesono))
updater.dispatcher.add_handler(CommandHandler('dovesiamo', dovesiamo))
updater.dispatcher.add_handler(CommandHandler('15240100103043', opera_solved))
updater.dispatcher.add_handler(
    MessageHandler(
        ~telegram.ext.filters.Filters.location,
        forward))
updater.dispatcher.add_handler(
    MessageHandler(
        telegram.ext.filters.Filters.location,
        update_latest_positions))
updater.start_polling(poll_interval=1)
updater.idle()
