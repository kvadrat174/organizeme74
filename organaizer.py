#!/usr/bin/env python

import datetime
import gspread
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import telebot
import datetime
import gsmod
import conf1
import requests
import os
import gsmod as gm
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

sh = gspread.authorize(credentials)

#wks = sh.open("testlist").sheet1
a=int()
wks= gm.id_check(a)




bot = telebot.TeleBot(conf1.TOKEN)



"""val = wks.acell('B1').value
val1 = wks.cell(1, 3).value
today = datetime.datetime.now()
print(val, val1, today.strftime("%m/%d/%Y"))

cell = wks.find("300")


print(cell.row, cell.col)"""




# НАБОР КЛАВИАТУР
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
bt1 = telebot.types.KeyboardButton('Добавить приход')
bt2 = telebot.types.KeyboardButton('Добавить расход')
bt3 = telebot.types.KeyboardButton('Статистика')
keyboard1.add(bt1, bt2, bt3)
keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
bt4 = telebot.types.KeyboardButton('Подтвердить приход')
bt5 = telebot.types.KeyboardButton('Исправить приход')
keyboard2.add(bt4, bt5)
keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
bt6 = telebot.types.KeyboardButton('Аренда')
bt7 = telebot.types.KeyboardButton('Материалы')
bt8 = telebot.types.KeyboardButton('Кредит')
bt9 = telebot.types.KeyboardButton('Личные нужды')
bt10 = telebot.types.KeyboardButton('ЗП')
bt11 = telebot.types.KeyboardButton('Логистика')
bt12 = telebot.types.KeyboardButton('Оборудование')
keyboard3.add(bt6,bt7,bt8,bt9,bt10,bt11,bt12)
keyboard4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
bt13 = telebot.types.KeyboardButton('Подтвердить расход')
bt14 = telebot.types.KeyboardButton('Исправить расход')
keyboard4.add(bt13, bt14)

# Приветственная речь
@bot.message_handler(commands=['start'])
def start_message(message):
    nm = message.from_user.first_name
    global wks
    global tu
    # надо исправить функцию и после отбора выводить не команду а айди документа, который надо открыть
    tu = message.from_user.id
    wks = gm.id_check(tu);
    #wks=sh.open(a).sheet1;





    bot.send_message(message.chat.id, 'Здравствуйте, ' +str(nm)+ ' , давайте упорядочим ваши финансы!', reply_markup=keyboard1);

@bot.message_handler(content_types=['text'])
def send_text(message):
    global metod
    tu = message.from_user.id
    wks = gm.id_check(tu)
        # Набор условий приход
    if message.text.lower() == 'добавить приход':
        tm = message.message_id

        tu = message.from_user.id
        nm = message.from_user.first_name

        bot.send_message(conf1.bossid,''+str(nm)+' , '+str(tu)+'')
        costs(message)
    elif message.text.lower() == 'подтвердить приход':
        bot.send_message(message.chat.id, 'Данные добавлены', reply_markup=keyboard1);
        val = wks.cell(1, 1).value
        val1 = (int(val) + 1);
        gm.income1(1, 1, val1);
    elif message.text.lower() == 'исправить приход':

        costs(message);
        # Набор условий расход
    elif message.text.lower() == 'добавить расход':
        bot.send_message(message.chat.id,'Укажите статью расходов', reply_markup=keyboard3);
    elif message.text.lower() == 'аренда':
        metod = 'аренда';
        rashod(message);
    elif message.text.lower() == 'материалы':
        metod = 'материалы';
        rashod(message);
    elif message.text.lower() == 'кредит':
        metod = 'кредит';
        rashod(message);
    elif message.text.lower() == 'личные нужды':
        metod = 'личные нужды';
        rashod(message);
    elif message.text.lower() == 'зп':
        metod = 'ЗП';
        rashod(message);
    elif message.text.lower() == 'логистика':
        metod = 'логистика';
        rashod(message);
    elif message.text.lower() == 'оборудование':
        metod = 'оборудование';
        rashod(message);
    # ПОДТВЕРЖДАЕМ РАСХОД
    elif message.text.lower() == 'подтвердить расход':
        bot.send_message(message.chat.id, 'Данные добавлены', reply_markup=keyboard1);
        val = wks.cell(1, 5).value
        val1 = (int(val) + 1);
        gm.income1(1, 5, val1);
    elif message.text.lower() == 'исправить приход':

        rashod(message);
    #Статистика
    elif message.text.lower() == 'статистика':
        ras= wks.cell(2,9).value
        doh= wks.cell(2,4).value
        bot.send_message(message.chat.id, 'На данный момент вы заработали '+str(doh)+'р. и потратили '+str(ras)+'р.',reply_markup=keyboard1)

# Прием ПРИХОД
@bot.message_handler(content_types=['text'])
def costs(message):
            bot.send_message(message.chat.id, "Введите сумму");
            bot.register_next_step_handler(message, get_income);

def get_income(message):  # получаем сумму
            global income;
            income = message.text;
            bot.send_message(message.chat.id, 'Откуда бабло?');
            bot.register_next_step_handler(message, get_otcuda);

def get_otcuda(message): # получаем
            global otcuda;

            otcuda = message.text;
            tu = message.from_user.id
            wks = gm.id_check(tu)
            nm = message.from_user.first_name
            income1 = income;
            otcuda1 =otcuda;
            bot.send_message(message.chat.id, '' +str(nm)+ ', вы подтверждаете внесение в таблицу ' + income + ' рублей за ' + str(otcuda) + '?', reply_markup=keyboard2)
            val = int()
            day = datetime.datetime.now()
            today = str(day.strftime("%m/%d/%Y"))
            val = wks.cell(1, 1).value
            gm.income1(val,1,today);
            gm.income1(val,2,income);
            gm.income1(val,3,otcuda);


# Прием расход
@bot.message_handler(content_types=['text'])
def rashod(message):
            bot.send_message(message.chat.id, "Введите сумму");
            bot.register_next_step_handler(message, get_outcome);

def get_outcome(message):  # получаем сумму
            global outcome;
            outcome = message.text;
            bot.send_message(message.chat.id, 'Напишите комментарий!');
            bot.register_next_step_handler(message, get_otcuda1);

def get_otcuda1(message): # получаем
            global otcuda;
            otcuda = message.text;
            nm = message.from_user.first_name
            tu = message.from_user.id
            wks = gm.id_check(tu)
            income1 = outcome;
            otcuda1 =otcuda;
            bot.send_message(message.chat.id, '' +str(nm)+ ', вы подтверждаете внесение в таблицу ' + outcome + ' рублей за ' + str(otcuda) + '?', reply_markup=keyboard4)
            val = int()
            day = datetime.datetime.now()
            today = str(day.strftime("%m/%d/%Y"))
            val = wks.cell(1, 5).value
            gm.income1(val,8,metod);
            gm.income1(val,5,today);
            gm.income1(val,6,outcome);
            gm.income1(val,7,otcuda);
            """val1 = (int(val) +1);
            gm.income1(1,5,val1);"""






bot.polling(none_stop=True, interval=0)
