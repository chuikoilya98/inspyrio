import requests
import json
import os.path as pt

class Bot() :

    def getToken(self):
        with open(pt.abspath('info/credentials.json'), 'r') as file :
            creds = json.load(file)
            token = creds['token']

            return token

    def sendMessage(self, text:str , chatId:str) -> bool :
        url = f'https://api.telegram.org/bot{self.getToken()}/sendMessage'
        params = {
            'chat_id' : chatId,
            'text' : text
        }
        req = requests.get(url=url, params=params)

        if req.status_code == 200 :
            return True
        else :
            return False

    def getTextByCommand(self, command:str) -> str:
        result = ''
        with open(pt.abspath(f'info/lang/ru/{command}.txt'), 'r') as file:
            for line in file :
                result += line
        return result

class MessageHandler():

    def isCommand(self, data:dict) -> dict :
        try :
            command = data['message']['entities'][0]['type']
            if command == 'bot_command' :
                result = {
                'isCommand' : 'true',
                'command' : data['message']['text']
                }
                return result
            else:
                result = {
                'isCommand' : 'false'
            }
                return result
        except KeyError :
            result = {
                'isCommand' : 'false'
            }
            return result

    def getUserInfo(self, data:dict) -> dict :
        userInfo = {
            'id' : data['message']['chat']['id'],
            'firstName' : data['message']['chat']['first_name'],
            'lastName' : data['message']['chat']['last_name'],
            'username' : data['message']['chat']['username'],
        }

        return userInfo

    def commandStart(self, data:dict) :
        userInfo = self.getUserInfo(data)
        #TODO: создание юзера в бд
        bot= Bot()
        text = bot.getTextByCommand(command='start')
        

k = Bot()
text  =  k.getTextByCommand('start')
k.sendMessage(text, '331392389')

