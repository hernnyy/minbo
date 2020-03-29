# -*- coding: utf-8 -*-
'''
Código generado por AlHerTa enbase al codigo de la Comunidad Minka-IT para el bot *minbo*.
TelegramBot: @AlhetaBot
BotName: alherta
'''

from py_expression_eval import Parser
from suds.client import Client
#from lbcapi import api
import telebot, os, aiml, sys, wikipedia
import texts, botstokens
import httplib2, logging
from telebot import types
import pyrebase
import datetime


#reload(sys)
#sys.setdefaultencoding('utf8')

#wikipedia set
wikipedia.set_lang("es")

#conn = api.hmac(botstokens.hmacTokens['hmac_key'], botstokens.hmacTokens['hmac_secret'])

bot = telebot.TeleBot(botstokens.tokens['alherta'])

logger = telebot.logger
telebot.logger.setLevel(logging.INFO) 
parser = Parser()

client = Client(url='http://www.banguat.gob.gt/variables/ws/TipoCambio.asmx?WSDL')
##client.set_options()

#firebase = pyrebase.initialize_app(botstokens.configFirebase)
### Get a reference to the auth service
#auth = firebase.auth();
#db = firebase.database();

# aiml: Cargar el kernel, setear valores y aprender conocimiento
#kernel = aiml.kernel()
#kernel.setBotPredicate('name', 'Alherta')
#kernel.setBotPredicate('nombre_bot', 'AlhetaBot')
#kernel.setBotPredicate('master', 'AlHerTa')
#kernel.setBotPredicate('botmaster', 'AlHerTa')
#kernel.setBotPredicate('ciudad', 'El Mundo')
#kernel.setBotPredicate('edad', '25')
#kernel.learn("aiml/sara/sara_srai_1.aiml")
#kernel.learn("aiml/sara/sara_srai_2.aiml")
#kernel.learn("aiml/sara/nombres.aiml")
#kernel.learn("aiml/sara/default.aiml")
#kernel.learn("aiml/sara/numeros.aiml")
#kernel.learn("aiml/sara/sexo.aiml")
#kernel.learn("aiml/sara/sara.aiml")

def listener(messages):
    for m in messages:
        chat_id = m.chat.id # Obtenemos el ID del chat (cada chat tiene uno único)
        texto = m.text      # y el texto que se nos ha enviado
#        print('ID: ' + str(chat_id) + ' MENSAJE: ' + texto) 
        logger.info("Nuevo mensaje recibido") # Sólo un mensaje en consola para que avise cuando haya un nuevo msj

bot.set_update_listener(listener)

#@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
@bot.message_handler(content_types=['new_chat_member'])
def on_user_joins(message):
    name = message.new_chat_member.first_name
    print (name)
    #if hasattr(message.new_chat_member, 'last_name') and message.new_chat_member.last_name is not None:
    if message.new_chat_member.last_name is not None:
        name += u" {}".format(message.new_chat_member.last_name)
        print ("Nuevo miembro en el grupo")
        print (name)

    #if hasattr(message.new_chat_member, 'username') and message.new_chat_member.username is not None:
    if message.new_chat_member.username is not None:
        name += u" (@{})".format(message.new_chat_member.username)
        print ("Nuevo miembro en el grupo")
        print (name)

    chat_id = message.chat.id
    bot.reply_to(message, texts.text_messages['bienvenido'].format(name=name))
#    bot.send_message(chat_id, texts.text_messages['bienvenido'].format(name=name))

@bot.message_handler(commands=['info', 'help'])
def on_info(message):
    chat_id = message.chat.id
    #bot.reply_to(message, texts.text_messages['info']) # respondemos con el mensaje correspondiente a info que está en el diccionario
    bot.send_message(chat_id, texts.text_messages['info']) # respondemos con el mensaje correspondiente a info que está en el diccionario

@bot.message_handler(commands=['hola', 'help'])
def on_hola(message):
    chat_id = message.chat.id
    name = message.chat.username
    bot.send_message(chat_id, texts.text_messages['hola'].format(name=name)) 

@bot.message_handler(commands=["ping"])
def on_ping(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Aquí estoy, vivito y coleando!")

@bot.message_handler(commands=['acercade'])
def send_acercade(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Somos la comunidad Minka-IT, un espacio formado por y para estudiantes de carreras informáticas\nde la Facultad de Ingeniería de la U.N.Ju. Aquí podrás plantear tus ideas, proyectos, compartir\ntu conocimiento y aprender cosas nuevas relacionadas con la informática.')

@bot.message_handler(commands=['documentos'])
def send_documentos(message):
    chat_id = message.chat.id
    #bot.reply_to(message, "Aquí puedes encontrar los documentos de la comunidad Minka-IT:\n http://bit.ly/24bon1o")
    bot.send_message(chat_id, "Aquí puedes encontrar los documentos de la comunidad Minka-IT:\nhttp://bit.ly/24bon1o")

@bot.message_handler(commands=['canales'])
def send_canales(message):
    chat_id = message.chat.id
    #bot.reply_to(message, "Minka en Facebook: http://bit.ly/1VGbO9g\nMinka en IRC: #minkait")
    bot.send_message(chat_id, "Minka en Facebook: http://bit.ly/1VGbO9g\nMinka en IRC: #minkait")

@bot.message_handler(commands=['dolar'])
def send_dolar(message):
    chat_id = message.chat.id
    request = client.factory.create('tns:Variables')
    request.variable = '29'
    response = client.service.Variables(request)
    cotizacion = str(response.CambioDia.Var[0].fecha) + "\nCompra: $" +str(response.CambioDia.Var[0].compra)+ "\nVenta: $" + str(response.CambioDia.Var[0].venta)
    bot.send_message(chat_id,cotizacion)

@bot.message_handler(commands=['tecla'])
def send_tecla(message):
    #markup = types.ReplyKeyboardRemove(selective=False)
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton(text='apple')
    itembtn2 = types.KeyboardButton('/bitcoins')
    itembtn3 = types.KeyboardButton('/dolar')
    itembtn4 = types.KeyboardButton('/tecla')
    itembtn5 = types.KeyboardButton('/draw sin(x)')
    itembtn6 = types.KeyboardButton('/cotiza')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)

@bot.message_handler(commands=['bitcoins'])
def send_bitcoins(message):
    chat_id = message.chat.id
    bot.send_chat_action(chat_id=chat_id, action='typing')
    #buys = conn.call('GET', '/buy-bitcoins-online/ARS/.json').json()
    #maxadd = minadd = buys["data"]["ad_list"][0]
    #maxval = float(0);
    #minval = float(minadd["data"]["temp_price_usd"]);
    #for adds in buys["data"]["ad_list"]:
    #    cval = float(adds["data"]["temp_price_usd"])
    #    if cval > maxval:
    #        maxval = cval
    #        maxadd = adds
    #    elif cval < minval:
    #        minval = cval
    #        minadd = adds
    #user = auth.sign_in_with_email_and_password(botstokens.userFirebase['user'],botstokens.userFirebase['pass'])
    #if (user):
    #    today = datetime.datetime.now()
    #    db.child("historial").child("{:%Y%m%d%H%M}".format(today)).child("minads").set(minadd,user['idToken'])
    #    db.child("historial").child("{:%Y%m%d%H%M}".format(today)).child("maxads").set(maxadd,user['idToken'])
    #bot.send_message(chat_id,"MAXIMO:\n\n"+str(maxadd))
    #bot.send_message(chat_id,"MINIMO:\n\n"+str(minadd))

@bot.message_handler(commands=['cotiza'])
def send_cotiza(message):
    chat_id = message.chat.id
    # keyboard = [[InlineKeyboardButton("Argentina", callback_data='29'), InlineKeyboardButton("Brasil", callback_data='13')]]

    # markup = InlineKeyboardMarkup(keyboard)

    # bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)
    bot.send_message(chat_id,"cotizacion")

# @bot.message_handler(commands=['reales'])
# def send_documentos(message):
#     chat_id = message.chat.id
#     conn = httplib2.Http()
#     headers = {
#   'content-type':'text/plain',
#   'Accept-Charset':'encoding=utf-8'
#     }
#     url_ = 'https://www.google.com/finance/converter?a=1000&from=BRL&to=ARS'
#     #query_args = { 'a':'1000', 'from':'BRL', 'to':'ARS' }
#     response = urllib2.urlopen(url_)
#     encoding = response.headers['content-type'].split('charset=')[-1]
#     ucontent = unicode(response.read(), encoding)
#     html = response.read()
#     response.close()  
#     #uri_ = '%s?%s' % (url_, urlencode('a=1000'))
#     #resp, content = conn.request(url_, "GET", headers)
#    # resp, content = conn.request("GET","http://www.google.com/finance/converter?a=1000&from=BRL&to=ARS",headers)
#     #for line in ucontent.encode('utf8'):
# # print line
#     if ucontent.encode('utf8').find('currency_converter_result') != -1:
#         print 'findit'
#   print ucontent.encode('utf8').find('currency_converter_result')
#   aux = ucontent[ucontent.find('currency_converter_result'):]
#   aux2 = aux[aux.find('<span class=bld>')+16:]
#   valor = aux2[:aux2.find('ARS')]
#     #print ucontent.encode('utf8')
#     bot.send_message(chat_id,valor)

@bot.message_handler(commands=['comm','command'])
def send_command(message):
    chat_id = message.chat.id
    param = message.text.split(' ',1)
    if len(param) == 1 or param[1]=="help":
        bot.send_message(chat_id,texts.text_messages['help_comm'])
    else:
        bot.send_message(chat_id, os.system(param[1]))

@bot.message_handler(commands=['drawx','draw'])
def send_draw(message):
    chat_id = message.chat.id
    msgid = message.message_id
    param = message.text.split(' ',1)
    if len(param) == 1 or param[1]=="help":
        bot.send_message(chat_id,texts.text_messages['help_draw'])
    else:
        readFile = open("simplefunctionsGNUP")
        lines = readFile.readlines()
        readFile.close()
        w = open("simplefunctionsGNUP",'w')
        w.writelines([item for item in lines[:-1]])
        w.close()
        with open('simplefunctionsGNUP', 'a') as file:
            file.write('plot [-10:10] '+param[1])
        #file.close()
    commands.getoutput('gnuplot -c simplefunctionsGNUP')
    #commands.getoutput("gnuplot -e 'plot [-10:10] '"+param[1])
    img = open('output.png', 'rb')
    bot.send_chat_action(chat_id, 'upload_photo')
    bot.send_photo(chat_id, img, reply_to_message_id=msgid)
    img.close()
    #bot.send_message(chat_id, )

@bot.message_handler(commands=['calc'])
def calc(message):
    chat_id = message.chat.id
    param = message.text.split(' ',1) #separa el comando de los parametros  
    if len(param) == 1 or param[1]=="help":
        bot.send_message(chat_id,texts.text_messages['help_calc'])
    else:
        try:    
            #bot.send_message(chat_id, ast.literal_eval(param[1]))
            bot.send_message(chat_id,parser.parse(param[1]).evaluate({}))
            print ("calc handler sucess: " + param[1])
        except Exception as e:
            bot.send_message(chat_id, "¡¡No podes calcular eso!!")
            print ("calc handler error: " + str(e) + ": " + param[1])

@bot.message_handler(commands=['chat','minbo'])
def chat(message):
    chat_id = message.chat.id
    param = message.text.split(' ',1) #separa el comando de los parametros
    if len(param) == 1 or param[1]=="help":
        bot.send_message(chat_id,texts.text_messages['help_chat'])
    else:
        try:
            print ("chat humano: " + param[1])
            respuesta=""#kernel.respond(param[1])
            print ("chat robot: " + respuesta)
            bot.send_message(chat_id,respuesta)
        except Exception as e:
            print (e)
            bot.send_message(chat_id,"Tengo un bug en mi estomago!")

@bot.message_handler(commands=['wiki','wikipedia'])
def wiki(message):
    chat_id = message.chat.id
    param = message.text.split(' ',1) #separa el comando de los parametros
    if len(param) == 1 or param[1]=="help":
        bot.send_message(chat_id,texts.text_messages['help_wiki'])
    else:
        bot.send_message(chat_id, "Consultando en Wikipedia...")
        try:
            wiki = wikipedia.page(param[1])
            bot.send_message(chat_id, wiki.summary)
            bot.send_message(chat_id, "Consulta mas en:\n"+wiki.url)
        except wikipedia.exceptions.DisambiguationError as e:
            bot.send_message(chat_id, "'"+param[1]+"'"+" puede referirse a:")
            bot.send_message(chat_id, '\n'.join(e.options))
        except wikipedia.exceptions.PageError as e:
            bot.send_message(chat_id, "No se encontro ninguna pagina, intenta con otra consulta!")
        except Exception as e:
            print (e)
            bot.send_message(chat_id,"Tengo un bug en mi estomago!")

    

bot.polling(none_stop=True,timeout=80)       # Iniciamos nuestro bot para que esté atento a los mensajes
