# coding=utf-8
import json
import random
import string
import urllib

import telegram

from commands import retry_on_telegram_error


def run(bot, chat_id, user, keyConfig, message, totalResults=1):
    requestText = message.replace(bot.name, "").strip()
    googurl = 'https://www.googleapis.com/customsearch/v1'
    args = {'cx': keyConfig.get('Google', 'GCSE_SE_ID'),
            'key': keyConfig.get('Google', 'GCSE_APP_ID'),
            'safe': "off",
            'q': requestText}
    realUrl = googurl + '?' + urllib.urlencode(args)
    data = json.load(urllib.urlopen(realUrl))
    if 'items' in data:
        imagelink = data['items'][0]['link']
        bot.sendMessage(chat_id=chat_id, text=requestText + ": " + imagelink)
    else:
        if 'error' in data:
            bot.sendMessage(chat_id=chat_id, text='I\'m sorry ' + (user if not user == '' else 'Dave') +
                                                  ' I got ' + data['error']['message'] + '.')
        else:
            bot.sendMessage(chat_id=chat_id, text='I\'m sorry ' + (user if not user == '' else 'Dave') +
                                                  ', I\'m afraid I can\'t find any links for ' +
                                                  string.capwords(requestText.encode('utf-8')))

