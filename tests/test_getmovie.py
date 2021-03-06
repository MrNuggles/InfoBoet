import ConfigParser
import unittest
import telegram

import commands.getmovie as getmovie


class TestGetMovie(unittest.TestCase):
    def test_getmovie(self):
        requestText = 'flight of the navigator'

        keyConfig = ConfigParser.ConfigParser()
        keyConfig.read(["keys.ini", "..\keys.ini"])
        bot = telegram.Bot(keyConfig.get('Telegram', 'TELE_BOT_ID'))
        chatId = keyConfig.get('BotAdministration', 'TESTING_GROUP_CHAT_ID')

        getmovie.run(bot, chatId, 'SalamiArmy', keyConfig, requestText)
