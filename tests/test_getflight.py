# coding=utf-8
import ConfigParser
import unittest
import telegram

import commands.getflight as getflight


class TestPlace(unittest.TestCase):
    def test_place(self):
        requestText = 'lucerne'

        keyConfig = ConfigParser.ConfigParser()
        keyConfig.read(["keys.ini", "..\keys.ini"])
        bot = telegram.Bot(keyConfig.get('Telegram', 'TELE_BOT_ID'))
        chatId = keyConfig.get('BotAdministration', 'TESTING_PRIVATE_CHAT_ID')

        getflight.run(bot, chatId, 'Admin', keyConfig, requestText)
