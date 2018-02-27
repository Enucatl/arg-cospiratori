import os
import telegram.ext
from telegram.ext import Updater
import click


@click.command()
@click.option("--chat_id", type=int)
def main(chat_id):
    token = os.environ["TOKEN"]
    print(chat_id)
    updater = Updater(token)
    updater.bot.send_audio(
        audio=open("dongiovanni.mp3", "rb"),
        chat_id=chat_id)


if __name__ == "__main__":
    main()
