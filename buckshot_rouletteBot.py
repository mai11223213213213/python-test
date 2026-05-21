import telebot
from telebot import types
from time import *
import random
import os
import datetime

token ="6798233570:AAHtFKEBm7HQ0AsoB4i4l6vY8P1yqL1fCRw"
bot=telebot.TeleBot(token)
print('жужа перемога')
shotgun_dmg ={}
magazine ={}
nbul = {}
bulets = {}
b=None
n=0
chat_play = []
cigatettes = {}
beer={}
saw={}
cuffs = {}
magfyi_glass = {}
time1 = 5
ldld = {}
curr_bul = {}
curr_move = {}
counter_rounds = {}
use_cuffs = {}





lifes = {}


def item_choice():
    l = 0
    a = None
    global cigatettes, beer, saw,cuffs,magfyi_glass
    item = [cigatettes, beer, saw, cuffs, magfyi_glass, ]


    while l != len(item):

        a = random.choice(item)


        a[user_id] = a[user_id] + 1
        l = l + 1
        print(item)
        if l == 3:
            break
    if l == 3:
        while l <= len(item) + 1:
            a = random.choice(item)
            a[user_id2] = a[user_id2] + 1
            l = l + 1
            print(item)
            if l == len(item) + 1:
               break
            print(item)
def buletss():
    global bulets
    chat_id = i.chat.id
    nbul[chat_id] = random.randint(1, 5)
    bulets[chat_id] = []
    n=0
    while n != nbul[chat_id]:
        b = random.randint(1,8)
        if b not in bulets[chat_id]:
            bulets[chat_id].append(b)
        else:
            n =n -1
        n = n + 1
    return bulets


@bot.message_handler(commands=['Contract'])
def start(message):
 global id, user_id, user_id2, i, username1, username2
 chat_id = message.chat.id
 i = message
 user_id = message.from_user.id
 username1 = bot.get_chat(user_id).username
 markup = types.InlineKeyboardMarkup(row_width=2)
 button = types.InlineKeyboardButton("прийняти", callback_data="yes")
 button1 = types.InlineKeyboardButton("відхилити", callback_data="no")
 markup.add(button, button1)
 beer[user_id] = 0
 saw[user_id] = 0
 cigatettes[user_id] = 0
 magfyi_glass[user_id] = 0
 cuffs[user_id] = 0







 if message.reply_to_message:
    user_id2 = message.reply_to_message.from_user.id
    beer[user_id2] = 0
    saw[user_id2] = 0
    cigatettes[user_id2] = 0
    magfyi_glass[user_id2] = 0
    cuffs[user_id2] = 0
    id = message.from_user.id
    username2 = bot.get_chat(user_id2).username
    users = [user_id, user_id2]
    if user_id != user_id2:
         if chat_id not in chat_play:
            chat_play.append(chat_id)
            print(chat_play)
            bot.send_message(message.chat.id, f"@{username1} пропонує вам зіграти в гру @{username2}",
                             reply_markup=markup)
            lifes[user_id] = 3
            lifes[user_id2] = 3
            magazine[chat_id] = [1,2,3,4,5,6,7,8]
            curr_move[chat_id] = random.choice(users)
            buletss()
            item_choice()
            use_cuffs[user_id] = 0
            use_cuffs[user_id2] = 0







         else:
           bot.send_message(message.chat.id, f"@{username1} тут вже гра є!")
    else:
          bot.send_message(message.chat.id, f"З собою не грають")



 else:
   bot.reply_to(message, f"@{username1} Nuh uh, з повітрям не грають")

@bot.message_handler(commands=['cancel'])
def cacellll(message):
    chat_id = message.chat.id
    if chat_id in chat_play:
        chat_id = message.chat.id
        bot.send_message(chat_id, f'Гру скасовано')
        chat_play.remove(chat_id)
        counter_rounds[chat_id] = 0

    else:
     bot.send_message(chat_id, f'Шоб гру скасувати її треба почати!!')



@bot.callback_query_handler(func=lambda call: call.data == "yes")
def gameStarted(call):
    global ldld

    call_id = call.from_user.id
    chat_id = i.chat.id

    if call_id == user_id2:
        bot.send_message(chat_id, 'Пропозиція прийнята')

        sleep(1)

        game()
    else:
        bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)





@bot.callback_query_handler(func=lambda call: call.data == "no")
def no(call):
  call_id = call.from_user.id
  if call_id == user_id2:
    chat_id = i.chat.id
    chat_play.remove(chat_id)
    counter_rounds[chat_id] = 0
    bot.send_message(chat_id, f'Пропозиція відхилена')
  else:
      bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)








def end():
    chat_id = i.chat.id
    if lifes[user_id] <= 0:
        bot.send_message(chat_id, f'Гру закінченно! переміг {username2}!')
        chat_play.remove(chat_id)
        counter_rounds[chat_id] = 0

    else:
        bot.send_message(chat_id, f'Гру закінченно! переміг {username1}!')
        chat_play.remove(chat_id)
        counter_rounds[chat_id] = 0




a = 0
qwqwqw = None
def game():
    global msg,ass,qwqwqw, curr_bul, nbul, shotgun_dmg,counter_rounds,aaaa, ban
    chat_id = i.chat.id
    print(lifes[user_id], lifes[user_id2])


    if chat_id  not in counter_rounds.keys():
            counter_rounds[chat_id] = 1
    else:
        counter_rounds[chat_id] = counter_rounds[chat_id] + 1

    qwqwqw = bot.get_chat(curr_move[chat_id]).username
    markup = types.InlineKeyboardMarkup(row_width=2)
    try:
     curr_bul[chat_id] = random.choice(magazine[chat_id])
    except IndexError:
     bot.send_message(chat_id, f'Патрони скінчилися!, перезарядка...')
     sleep(3)
     magazine[chat_id] = [1, 2, 3, 4, 5, 6, 7, 8]
     item_choice()
     nbul[chat_id] = random.randint(1,5)
     buletss()

    shotgun_dmg[chat_id] = 1
    use_cuffs[user_id] = 0
    use_cuffs[user_id2] = 0


    print(magazine[chat_id], len(magazine[chat_id]), bulets[chat_id], len(bulets[chat_id]))
    aaaa = bot.send_message(chat_id, f'Раунд {counter_rounds[chat_id]}:\n кіль-ть життів: @{username1}: {lifes[user_id]}, @{username2}: {lifes[user_id2]}\n Патрони:\n Справжні: {len(bulets[chat_id])} \n Холості:{len(magazine[chat_id]) - len(bulets[chat_id])}')
    sleep(2)
    button1 = types.InlineKeyboardButton("стріляти", callback_data="shot")
    button2= types.InlineKeyboardButton("предмети", callback_data="items")
    markup.add(button1,button2)
    msg = bot.send_message(chat_id, f'Хід {qwqwqw}',  reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "items")
def choseit(call):
    global msg_e
    chat_id = i.chat.id
    user_idd = call.from_user.id
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(f'Пиво:{beer[curr_move[chat_id]]}', callback_data="beer")
    button2 = types.InlineKeyboardButton(f"Пила: {saw[curr_move[chat_id]]}", callback_data="saw")
    button3 = types.InlineKeyboardButton(f"Сигарети: {cigatettes[curr_move[chat_id]]}", callback_data="cigari")
    button4 = types.InlineKeyboardButton(f"Лупа: {magfyi_glass[curr_move[chat_id]]}", callback_data="lupa")
    button5 = types.InlineKeyboardButton(f"Наручники: {cuffs[curr_move[chat_id]]}", callback_data="cufs")
    button6 = types.InlineKeyboardButton(f"Назад", callback_data="back")
    markup.add(button6)
    markup.add(button1, button2)
    markup.add(button3, button4, button5)


    if user_idd == curr_move[chat_id]:
        msg_e = bot.edit_message_text(chat_id=i.chat.id, message_id=msg.message_id,text=f'Предмети {qwqwqw}', reply_markup=markup)
    else:
        bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)

def lala():
    chat_id = i.chat.id
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(f'Пиво:{beer[curr_move[chat_id]]}', callback_data="beer")
    button2 = types.InlineKeyboardButton(f"Пила: {saw[curr_move[chat_id]]}", callback_data="saw")
    button3 = types.InlineKeyboardButton(f"Сигарети: {cigatettes[curr_move[chat_id]]}", callback_data="cigari")
    button4 = types.InlineKeyboardButton(f"Лупа: {magfyi_glass[curr_move[chat_id]]}", callback_data="lupa")
    button5 = types.InlineKeyboardButton(f"Наручники: {cuffs[curr_move[chat_id]]}", callback_data="cufs")
    button6 = types.InlineKeyboardButton(f"Назад", callback_data="back")
    markup.add(button6)
    markup.add(button1, button2)
    markup.add(button3, button4, button5)
    msg_e = bot.edit_message_text(chat_id=i.chat.id, message_id=msg.message_id, text=f'Предмети {qwqwqw}',
                                  reply_markup=markup)
    return markup, button1, button2, button3, button4, button5, button6

@bot.callback_query_handler(func=lambda call: call.data == "beer")
def beerr(call):
    chat_id = i.chat.id
    user_idd = call.from_user.id

    if user_idd == curr_move[chat_id]:
      if beer[curr_move[chat_id]] != 0:
        bot.send_message(chat_id, f'{bot.get_chat(curr_move[chat_id]).username} чік чікчірік гуп гуп бабах ууууу, патрон який висковив був...')
        if curr_bul[chat_id] in bulets[chat_id]:
            sleep(2)
            bot.send_message(chat_id,f'Справжнім 😮')
            magazine[chat_id].remove(curr_bul[chat_id])
            bulets[chat_id].remove(curr_bul[chat_id])
            beer[curr_move[chat_id]] = beer[curr_move[chat_id]] - 1
            curr_bul[chat_id] = random.choice(magazine[chat_id])
            lala()
            aaaa1 = bot.edit_message_text(chat_id=i.chat.id, message_id=aaaa.message_id, text=f'Раунд {counter_rounds[chat_id]}:\n кіль-ть життів: @{username1}: {lifes[user_id]}, @{username2}: {lifes[user_id2]}\n Патрони:\n Справжні: {len(bulets[chat_id])} \n Холості:{len(magazine[chat_id]) - len(bulets[chat_id])}')


        else:
            sleep(2)
            bot.send_message(chat_id, f'Холостим 😁')
            magazine[chat_id].remove(curr_bul[chat_id])
            curr_bul[chat_id] = random.choice(magazine[chat_id])
            beer[curr_move[chat_id]] = beer[curr_move[chat_id]] - 1
            lala()
            aaaa1 = bot.edit_message_text(chat_id=i.chat.id, message_id=aaaa.message_id, text=f'Раунд {counter_rounds[chat_id]}:\n кіль-ть життів: @{username1}: {lifes[user_id]}, @{username2}: {lifes[user_id2]}\n Патрони:\n Справжні: {len(bulets[chat_id])} \n Холості:{len(magazine[chat_id]) - len(bulets[chat_id])}')




      else:
          bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)






    else:
        bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data == "saw")
def was(call):
    global  shotgun_dmg
    chat_id = i.chat.id
    user_idd = call.from_user.id

    if user_idd == curr_move[chat_id]:
      if saw[curr_move[chat_id]] != 0:
        bot.send_message(chat_id, f"{bot.get_chat(curr_move[chat_id]).username} розрізав дробовик, тепер від б'є вдвічі бульше на один постріл")
        shotgun_dmg[chat_id] = 2
        saw[curr_move[chat_id]] = saw[curr_move[chat_id]] - 1
        lala()

      else:
          bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)
    else:
        bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)


@bot.callback_query_handler(func=lambda call: call.data == "cigari")
def cigarii(call):
    global shotgun_dmg
    chat_id = i.chat.id
    user_idd = call.from_user.id

    if user_idd == curr_move[chat_id]:
        if cigatettes[curr_move[chat_id]] != 0:
            bot.send_message(chat_id,
                             f"{bot.get_chat(curr_move[chat_id]).username} закуив(куріння шкідливе) і йому додалось 1 життя")
            lifes[curr_move[chat_id]] = lifes[curr_move[chat_id]] + 1
            cigatettes[curr_move[chat_id]] = cigatettes[curr_move[chat_id]] - 1
            lala()
            aaaa1 = bot.edit_message_text(chat_id=i.chat.id, message_id=aaaa.message_id, text=f'Раунд {counter_rounds[chat_id]}:\n кіль-ть життів: @{username1}: {lifes[user_id]}, @{username2}: {lifes[user_id2]}\n Патрони:\n Справжні: {len(bulets[chat_id])} \n Холості:{len(magazine[chat_id]) - len(bulets[chat_id])}')
            return lifes[curr_move[chat_id]]
        else:
            bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)
    else:
        bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data == "lupa")
def apul(call):

    chat_id = i.chat.id
    user_idd = call.from_user.id

    if user_idd == curr_move[chat_id]:
      if magfyi_glass[curr_move[chat_id]] != 0:
        bot.send_message(chat_id, f"Дуже цікаво.....")
        if curr_bul[chat_id] in bulets[chat_id]:
            bot.answer_callback_query(call.id, text='Я бачу.... смерть', show_alert=True)
        else:
            bot.answer_callback_query(call.id, text='Я бачу.... життя', show_alert=True)
        magfyi_glass[curr_move[chat_id]] = magfyi_glass[curr_move[chat_id]] - 1
        lala()

      else:
          bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)
    else:
        bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)



@bot.callback_query_handler(func=lambda call: call.data == "cufs")
def sus(call):
    global use_cuffs
    chat_id = i.chat.id
    user_idd = call.from_user.id

    if user_idd == curr_move[chat_id]:
      if cuffs[curr_move[chat_id]] != 0:
        bot.send_message(chat_id, f"{bot.get_chat(curr_move[chat_id]).username} надів начручники на оппонента, тепер він пропускає хід!")
        if curr_move[chat_id] == user_id:
          use_cuffs[user_id2] = 1
          print('1')
        else:
            use_cuffs[user_id] = 1
            print('11')

        cuffs[curr_move[chat_id]] = cuffs[curr_move[chat_id]] - 1
        lala()

      else:
          bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)
    else:
        bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)




@bot.callback_query_handler(func=lambda call: call.data == "shot")
def shot(call):
    global msg_e
    user_idd = call.from_user.id
    chat_id = i.chat.id
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(f"{username1}", callback_data="user1")
    button2 = types.InlineKeyboardButton(f"{username2}", callback_data="user2")
    button3 = types.InlineKeyboardButton(f"Назад", callback_data="back")
    markup.add(button1, button2)
    markup.add(button3)
    if user_idd == curr_move[chat_id]:
        msg_e = bot.edit_message_text(chat_id=i.chat.id, message_id=msg.message_id,text=f'Хід {qwqwqw}', reply_markup=markup)
    else:
        bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)














@bot.callback_query_handler(func=lambda call: call.data == "user1")
def shot1(call):
 global lifes, magazine
 user_idd = call.from_user.id
 chat_id = i.chat.id
 if user_idd == curr_move[chat_id]:
   if user_idd == user_id:
        bot.send_message(chat_id, f'{username1}, стріляє в себе!')
        if curr_bul[chat_id] in bulets[chat_id]:
            sleep(3)
            bot.send_message(chat_id, f'Дробовик виcтрелив.... справжнім патроном(f)')
            lifes[user_id] = lifes[user_id] - shotgun_dmg[chat_id]
            magazine[chat_id].remove(curr_bul[chat_id])
            bulets[chat_id].remove(curr_bul[chat_id])

            if use_cuffs[user_id2] == 0:
                curr_move[chat_id] = user_id2
            else:
                curr_move[chat_id] = user_id


            if lifes[user_id] <= 0 or lifes[user_id2] <=0:
                end()
                bot.delete_message(chat_id, msg_e.id)
            else:
                game()
                bot.delete_message(chat_id, msg_e.id)




        else:
            sleep(3)
            bot.send_message(chat_id, f'Дробовик виcтрелив.... холостим патроном!')
            magazine[chat_id].remove(curr_bul[chat_id])

            curr_move[chat_id] = user_id

            if lifes[user_id] <= 0 or lifes[user_id2] <= 0:
                end()
                bot.delete_message(chat_id, msg_e.id)
            else:
                game()
                bot.delete_message(chat_id, msg_e.id)

   else:
        bot.send_message(chat_id, f'{username2} стріляє в {username1}!')
        if curr_bul[chat_id] in bulets[chat_id]:
            sleep(3)
            bot.send_message(chat_id, f'Дробовик виcтрелив.... справжнім патроном(f)')
            lifes[user_id] = lifes[user_id] - shotgun_dmg[chat_id]
            magazine[chat_id].remove(curr_bul[chat_id])
            bulets[chat_id].remove(curr_bul[chat_id])

            if use_cuffs[user_id] == 0:
             curr_move[chat_id] = user_id
            else:
              curr_move[chat_id] = user_id2

            if lifes[user_id] <= 0 or lifes[user_id2] <= 0:
                end()
                bot.delete_message(chat_id, msg_e.id)
            else:
                game()
                bot.delete_message(chat_id, msg_e.id)




        else:
            sleep(3)
            bot.send_message(chat_id, f'Дробовик виcтрелив.... холостим патроном!')
            magazine[chat_id].remove(curr_bul[chat_id])
            if use_cuffs[user_id] == 0:
                curr_move[chat_id] = user_id
            else:
                curr_move[chat_id] = user_id2
            if lifes[user_id] <= 0 or lifes[user_id2] <= 0:
                end()
                bot.delete_message(chat_id, msg_e.id)
            else:
                game()
                bot.delete_message(chat_id, msg_e.id)
 else:
      bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)


@bot.callback_query_handler(func=lambda call: call.data == "user2")
def shot1(call):
 global lifes, magazine
 user_idd = call.from_user.id
 chat_id = i.chat.id
 if user_idd == curr_move[chat_id]:
   if user_idd == user_id2:
        bot.send_message(chat_id, f'{username2}, стріляє в себе!')
        if curr_bul[chat_id] in bulets[chat_id]:
            sleep(3)
            bot.send_message(chat_id, f'Дробовик виcтрелив.... справжнім патроном(f)')
            lifes[user_id2] = lifes[user_id2] - shotgun_dmg[chat_id]
            magazine[chat_id].remove(curr_bul[chat_id])
            bulets[chat_id].remove(curr_bul[chat_id])
            if use_cuffs[user_id] == 0:
                curr_move[chat_id] = user_id
            else:
                curr_move[chat_id] = user_id2


            if lifes[user_id] <= 0 or lifes[user_id2] <= 0:
                end()
                bot.delete_message(chat_id, msg_e.id)
            else:
                game()
                bot.delete_message(chat_id, msg_e.id)




        else:
            sleep(3)
            bot.send_message(chat_id, f'Дробовик виcтрелив.... холостим патроном!')
            magazine[chat_id].remove(curr_bul[chat_id])
            curr_move[chat_id] = user_id2
            if lifes[user_id] <= 0 or lifes[user_id2] <= 0:
                end()
                bot.delete_message(chat_id, msg_e.id)
            else:
                game()
                bot.delete_message(chat_id, msg_e.id)

   else:
        bot.send_message(chat_id, f'{username1} стріляє в {username2}!')
        if curr_bul[chat_id] in bulets[chat_id]:
            sleep(3)
            bot.send_message(chat_id, f'Дробовик виcтрелив.... справжнім патроном(f)')
            lifes[user_id2] = lifes[user_id2] - shotgun_dmg[chat_id]
            magazine[chat_id].remove(curr_bul[chat_id])
            bulets[chat_id].remove(curr_bul[chat_id])
            if use_cuffs[user_id2] == 0:
                curr_move[chat_id] = user_id2
                print(curr_move)
            else:
                curr_move[chat_id] = user_id
                print(curr_move)
            if lifes[user_id] <= 0 or lifes[user_id2] <= 0:
                end()
                bot.delete_message(chat_id, msg_e.id)
            else:
                game()
                bot.delete_message(chat_id, msg_e.id)



        else:
            sleep(3)
            bot.send_message(chat_id, f'Дробовик виcтрелив.... холостим патроном!')
            magazine[chat_id].remove(curr_bul[chat_id])
            if use_cuffs[user_id2] == 0:
             curr_move[chat_id] = user_id2
            else:
              curr_move[chat_id] = user_id
            if lifes[user_id] <= 0 or lifes[user_id2] <= 0:
                end()
                bot.delete_message(chat_id, msg_e.id)
            else:
                game()
                bot.delete_message(chat_id, msg_e.id)
 else:
        bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)


@bot.callback_query_handler(func=lambda call: call.data == "back")
def back(call):
    chat_id = i.chat.id
    user_idd = call.from_user.id
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton("стріляти", callback_data="shot")
    button2 = types.InlineKeyboardButton("предмети", callback_data="items")
    markup.add(button1,button2)
    if user_idd == curr_move[chat_id]:
        msg = bot.edit_message_text(chat_id=i.chat.id, message_id=msg_e.message_id, text=f'Хід {qwqwqw}', reply_markup=markup)
    else:
        bot.answer_callback_query(call.id, text='Nuh uh', show_alert=True)






































bot.infinity_polling(none_stop=True)