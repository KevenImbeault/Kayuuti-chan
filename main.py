#Author : Keven Imbeault
#Creation date : 08/03/2019
#Description : Main code of the bot

import discord
from discord.utils import get

f = open('Bot_Credentials.txt', 'r') 

TOKEN = f.readline().rstrip("\n\r")

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!live') and message.channel == get(client.get_all_channels(), server__name='Keven\'s comfy server' , id='558789671828848650'):
        Stream_Annoucements_Channel = get(client.get_all_channels(), server__name='Keven\'s comfy server' , id='523706122880942103')

        msg = message.content.replace('!live ', '') + ' @everyone'

        await client.send_message(Stream_Annoucements_Channel, msg)

#Says the name and id of the bot it's connected to
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------')

client.run(TOKEN)