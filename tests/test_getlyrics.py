import ConfigParser
import unittest
import telegram

import commands.getlyrics as getlyrics


class TestGetLyrics(unittest.TestCase):
    def test_getlyrics(self):
        requestText = 'yes fuck me up I\'ve been a whore'

        keyConfig = ConfigParser.ConfigParser()
        keyConfig.read(["keys.ini", "..\keys.ini"])
        bot = telegram.Bot(keyConfig.get('Telegram', 'TELE_BOT_ID'))
        chatId = keyConfig.get('BotAdministration', 'TESTING_PRIVATE_CHAT_ID')

        getlyrics.run(bot, chatId, 'Admin', keyConfig, requestText)
