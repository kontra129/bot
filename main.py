import telebot
from telebot import types

bot = telebot.TelegramBot('')

@bot.message_handler(commands=['start'])
def main(message):
    #-------button--------
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('🤔Мини-курсы🤔')
    btn2 = types.KeyboardButton('✅Индивидуальные услуги✅')
    markup.row(btn1, btn2)
    if message.text == "❌Отмена❌":
        bot.send_message(message.chat.id, "😥Напишите пожалуйста, что вам не понравилось: @Agres_sive 😥")
    if message.text == "✅Готово✅":
        bot.send_message(message.chat.id, "😎Надеемся, что вам понравится😎")
    if message.text == 'никиталох':
        bot.send_message(message.chat.id, f'Согласен с тобой {message.from_user.first_name} ')
    bot.send_message(message.chat.id, f'✋Привет {message.from_user.first_name}, сначало выбери услугу⬇', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

@bot.message_handler(content_types=['text'])
def on_click(message):
    # ------------индивидуальные-услуги---------------------
    if message.text == "✅Индивидуальные услуги✅":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btns = types.KeyboardButton('🍚сушка🍚')
        markup.row(btns)
        btnn = types.KeyboardButton('🍗набор🥩')
        markup.row(btnn)
        btni = types.KeyboardButton('❓Свой вариант ответа❓')
        markup.row(btni)
        print("Индивидуальные-услуги")
        bot.send_message(message.chat.id, 'Что вы хотите достичь? ', reply_markup=markup)
        bot.register_next_step_handler(message, wait1)

    # ------------мини-курсы---------------------
    if message.text == "🤔Мини-курсы🤔":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn3 = types.KeyboardButton('✔ягодицы✔')
        markup.row(btn3)
        btn4 = types.KeyboardButton('💪бицепс💪')
        markup.row(btn4)
        btn5 = types.KeyboardButton('👍спина👍')
        markup.row(btn5)
        btn6 = types.KeyboardButton('🍚сушка🍚')
        markup.row(btn6)
        btn7 = types.KeyboardButton('🍗набор🥩')
        markup.row(btn7)
        print("мини-курсы")
        bot.send_message(message.chat.id, 'Что вы хотите достичь? ', reply_markup=markup)
        bot.register_next_step_handler(message, wait)

# ------------индивидуальные-услуги---------------------
@bot.message_handler(content_types=['text'])
def wait1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btnd = types.KeyboardButton('✅Готово✅')
    markup.row(btnd)
    btnc = types.KeyboardButton('❌Отмена❌')
    markup.row(btnc)
    if message.text == "🍚сушка🍚":
        bot.send_message(message.chat.id, '✅Готово✅')
        bot.send_message(message.chat.id,
                         "⬇Скопируйте пожалуйста эти сообщение и перешлите нашему тренеру: @Agres_sive ⬇")
        bot.send_message(message.chat.id, '✅Цена:4000р-месяц✅')
        bot.send_message(message.chat.id, "✅Вы выбрали: сушка (индивидуальная-услуга)✅", reply_markup=markup)
    if message.text == "🍗набор🥩":
        bot.send_message(message.chat.id, '✅Готово✅')
        bot.send_message(message.chat.id,
                         "⬇Скопируйте пожалуйста эти сообщение и перешлите нашему тренеру: @Agres_sive ⬇")
        bot.send_message(message.chat.id, '✅Цена:4000р-месяц✅')
        bot.send_message(message.chat.id, "✅Вы выбрали: набор (индивидуальная-услуга)✅", reply_markup=markup)
    if message.text == "❓Свой вариант ответа❓":
        bot.send_message(message.chat.id, '✅Готово✅')
        bot.send_message(message.chat.id,
                         "➡Напишите нашему тренеру: @Agres_sive ⬅", reply_markup=markup)
    bot.register_next_step_handler(message, main)

#------------мини-курсы---------------------
@bot.message_handler(content_types=['text'])
def wait(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn8 = types.KeyboardButton('✅Готово✅')
    markup.row(btn8)
    btn9 = types.KeyboardButton('❌Отмена❌')
    markup.row(btn9)
    if message.text == "✔ягодицы✔":
        bot.send_message(message.chat.id, '✅Готово✅')
        bot.send_message(message.chat.id, "⬇Скопируйте пожалуйста эти сообщение и перешлите нашему тренеру: @Agres_sive ⬇")
        bot.send_message(message.chat.id, '✅Цена:199р✅')
        bot.send_message(message.chat.id, "✅Вы выбрали: ягодицы✅", reply_markup=markup)
    if message.text == "💪бицепс💪":
        bot.send_message(message.chat.id, '✅Готово✅')
        bot.send_message(message.chat.id, "⬇Скопируйте пожалуйста эти сообщение и перешлите нашему тренеру: @Agres_sive ⬇")
        bot.send_message(message.chat.id, '✅Цена:199р✅')
        bot.send_message(message.chat.id, "✅Вы выбрали: бицепс✅", reply_markup=markup)
    if message.text == "👍спина👍":
        bot.send_message(message.chat.id, '✅Готово✅')
        bot.send_message(message.chat.id, "⬇Скопируйте пожалуйста эти сообщение и перешлите нашему тренеру: @Agres_sive ⬇")
        bot.send_message(message.chat.id, '✅Цена:199р✅')
        bot.send_message(message.chat.id, "✅Вы выбрали: спина✅", reply_markup=markup)
    if message.text == "🍚сушка🍚":
        bot.send_message(message.chat.id, '✅Готово✅')
        bot.send_message(message.chat.id, "⬇Скопируйте пожалуйста эти сообщение и перешлите нашему тренеру: @Agres_sive ⬇")
        bot.send_message(message.chat.id, '✅Цена:199р✅')
        bot.send_message(message.chat.id, "✅Вы выбрали: сушка✅", reply_markup=markup)
    if message.text == "🍗набор🥩":
        bot.send_message(message.chat.id, '✅Готово✅')
        bot.send_message(message.chat.id, "⬇Скопируйте пожалуйста эти сообщение и перешлите нашему тренеру: @Agres_sive ⬇")
        bot.send_message(message.chat.id, '✅Цена:199р✅')
        bot.send_message(message.chat.id, "✅Вы выбрали: набор✅", reply_markup=markup)
    bot.register_next_step_handler(message, main)



bot.infinity_polling()
