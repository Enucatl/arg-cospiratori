import logging
from decorator import decorator
import numpy as np
import telegram.ext
import collections
import datetime


logger = logging.getLogger(__name__)

my_chat_id = 62030274


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


@decorator
def forward(f, bot, update):
    if update.message.chat.id > 0:
        chat_name = update.message.chat.first_name
    else:
        chat_name = update.message.chat.title
    bot.send_message(
        chat_id=my_chat_id,
        text="{} ({}, {}): {}".format(
            update.message.from_user.first_name,
            chat_name,
            update.message.chat.id,
            update.message.text))
    replies = f(bot, update)
    if isinstance(replies, collections.Iterable):
        for r in replies:
            r.forward(chat_id=my_chat_id)
    else:
        replies.forward(chat_id=my_chat_id)
    return replies


@forward
def help(bot, update):
    return update.message.reply_text(
        """
c'è una cosa che è successa a cui dovete rimediare...
chi è??? NOOOO... FERMI COSA FATE!!!!! ahhhhh!



Siete stati scoperti, avete dieci giorni per riattivare
i sacri pilastri... altrimenti verremo a prendere
anche voi HAHAHAHAHAHAHAHAHA!
        """)


@forward
def pilastri(bot, update):
    r1 = update.message.reply_text(
        text="""
*Fu antico test*
Vi do inganno:
delfini, gazze, oro
        """,
        parse_mode=telegram.ParseMode.MARKDOWN,
        quote=False)
    r2 = update.message.reply_text(
        text="/anni 🇮🇹 🇫🇷 ***",
        quote=False)
    return r1, r2


@forward
def ichbin(bot, update):
    return update.message.reply_text(
        text="eh ... dovesei ????")



@forward
def id_max(bot, update):
    return update.message.reply_text(
        text="non conosco l'identità segreta... è nella lista dei cospiratori ricercati")



@forward
def cospiratori(bot, update):
    return update.message.reply_text(
        text="""
🇨🇭 = 85010254, 45006035
🇫🇷 = 127145721
🇩🇪 = 82200874
🇮🇹 = 85218517
        """)



@forward
def abulafia(bot, update):
    return update.message.reply_text(
        text="""
Sediento de saber lo que Dios sabe,
Judá León se dio a permutaciones de letras
y complejas variaciones
y al fin pronunció el Nombre que es la Clave
        """)


@forward
def borges(bot, update):
    return update.message.reply_text(
        text="If you torture words enough, they'll confess to anything.")


@forward
def sbahn(bot, update):
    r = update.message.reply_audio(
        open("sound.m4a", "rb"),
    )       
    return r


@forward
def mozart(bot, update):
    r = update.message.reply_audio(
        open("delfinigazzeoro.mp3", "rb"),
    )       
    return r


@forward
def magdalena(bot, update):
    return update.message.reply_text(
        text="non ho tempo per queste cose, devo incontrarmi con l'agente {}".format(ids["Massimo"]))


@forward
def lenozzedifigaro(bot, update):
    return update.message.reply_text(
        text="5 * 20 * 36 *")


@forward
def ostkreuz(bot, update):
    return update.message.reply_text(
        text="ma dovesei ?")


@forward
def dongiovanni(bot, update):
    return update.message.reply_text(
        text="91 100 231 640 1003")


@forward
def cosifantutte(bot, update):
    return update.message.reply_text(
        text="anni 1 100 1000")


@forward
def opera_solved(bot, update):
    return update.message.reply_text(
        """
OFLGU210
        """
    )


@forward
def mozartlaugh(bot, update):
    return update.message.reply_video(
        open("mozart.mp4", "rb")
    )


@forward
def oflgu210(bot, update):
    return update.message.reply_photo(
        open("photo_2018-02-25_15-06-10.jpg", "rb"),
        quote=False
    )


@forward
def anni(bot, update):
    return update.message.reply_photo(
        open("abulafia.png", "rb"),
        quote=False
    )


@forward
def croce_oriente(bot, update):
    return update.message.reply_text(
        """
portami ai piedi
della croce d'oriente

dovesono ?
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


@forward
def dovesono(bot, update):
    check_positions_in_last_hour()
    replies = []
    chosen = "Massimo"
    if (update.message.from_user.id == ids[chosen]
        and ids[chosen] in position_dictionary):
        ostkreuz = {
            "lat": 52.503267,
            "lon": 13.469323
        }
        d = distance(
            position_dictionary[ids[chosen]]["lat"],
            position_dictionary[ids[chosen]]["lon"],
            ostkreuz["lat"],
            ostkreuz["lon"])
        r1 = update.message.reply_text(
            "{} km".format(d),
            quote=False)
        replies.append(r1)
        if d < 0.2:
            r2 = update.message.reply_photo(
                open("dovesiamo.jpg", "rb"),
                quote=False)
            replies.append(r2)
    else:
        r3 = update.message.reply_text(
            "Impossibile localizzare l'agente {}".format(ids[chosen]))
        replies.append(r3)
    return replies


@forward
def dovesiamo(bot, update):
    replies = []
    deleted_keys = check_positions_in_last_hour()
    for key in deleted_keys:
        r = update.message.reply_text(
            "agente {} disperso".format(key),
            quote=False)
        replies.append(r)
    total_distance = 0
    for target in targets:
        if not target in position_dictionary:
            update.message.reply_text(
                "Impossibile localizzare l'agente {}".format(target))
            return
        else:
            total_distance += distance(
                position_dictionary[target]["lat"],
                position_dictionary[target]["lon"],
                targets[target]["lat"],
                targets[target]["lon"])
    r1 = update.message.reply_text(
        "{} km".format(total_distance),
        quote=False)
    replies.append(r1)
    if total_distance < 0.5:
        r2 = update.message.reply_text(
            "https://www.youtube.com/watch?v=04854XqcfCY",
            quote=False)
        replies.append(r2)
    return replies


@forward
def do_nothing(bot, update):
    return []
    

position_dictionary = {}
@forward
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
    return []


def check_positions_in_last_hour():
    deleted_keys = []
    for key, value in position_dictionary.items():
        if (value["timestamp"] - datetime.datetime.now()).total_seconds() > 900:
            del position_dictionary[key]
            deleted_keys.append(key)
    return deleted_keys
