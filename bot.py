import os

import telebot
from nltk.corpus import wordnet


BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['meaning', 'give me world'])
def action_meaning(message):
    sent_msg = bot.send_message(message.chat.id, "Please tell me one word")
    bot.register_next_step_handler(sent_msg, meaning_text)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Hi, I am here to help you."
        "If you want to know mean and synonym and antonym of the word use"
        " this command /meaning"
    )


def meaning_text(message):
    print('text ', message.text)
    if message.text == '/start':
        bot.register_next_step_handler(send_welcome)
    if message.text == '/meaning':
        bot.register_next_step_handler(action_meaning)

    syn = wordnet.synsets(message.text)
    synonyms = []
    antonyms = []
    for s in syn:
        for lm in s.lemmas():
            if lm.name() not in synonyms:
                synonyms.append(lm.name())
            if lm.antonyms():
                if lm.antonyms()[0].name() not in antonyms:
                    antonyms.append(lm.antonyms()[0].name())

    text = f'The meaning: {syn[0].definition()}, \n\n Synonym: {synonyms},' \
           f'\n\n antonyms: {antonyms}'
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, meaning_text)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()

