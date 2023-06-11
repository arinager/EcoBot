import random

import discord
from discord.ext import commands

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$Как мне сортировать мусор?'):
        await message.channel.send("Это не так уж и тяжело на самом деле. Вы можете: 1.Купить домой 2 мусорных ведр и в одно выбрасывать пласти, а в другое стекло и выкидывать их в соответствующие контейнеры.")
    if message.content.startswith('$Что делать, что бы приборы не ломались раньше времени?'):
        await message.channel.send("На самом деле, на инструкции по большей части есть вся информация, но за частую, их просто нужно ограничивать от пыли и держать по дальше от воды.")
    if message.content.startswith('$Что делать со сломанными приборами?'):
        await message.channel.send("Лучше относите их к мастеру, но если предмет нельзя починить, отвозите их на переработку.")
    elif message.content.startswith('$Спасибо! Пока'):
        await message.channel.send("\\")
    else:
        await message.channel.send(message.content)

client.run("MTEwOTg0MjI1MDE0MzM3MTMzNA.GOyj8L.lHUS6Ms8sQQVG8F1cGU5Mq-Lg3dEVn_TUPMPpU")