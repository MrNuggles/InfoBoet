import ConfigParser
import unittest
import telegram

import commands.getquote as getquote


class TestGetQuote(unittest.TestCase):
    def test_getquote(self):
        requestText = 'I will fuck you up'

        keyConfig = ConfigParser.ConfigParser()
        keyConfig.read(["keys.ini", "..\keys.ini"])
        bot = telegram.Bot(keyConfig.get('Telegram', 'TELE_BOT_ID'))
        chatId = keyConfig.get('BotAdministration', 'TESTING_PRIVATE_CHAT_ID')

        getquote.run(bot, chatId, 'Admin', keyConfig, requestText)
