import discord, datetime, random, os,re
import asyncio
from bs4 import BeautifulSoup
from Modules.Help import *
from Modules.Search import Search


client = discord.Client()
token = "NTQzMDU5ODQ2MTE5ODE3MjE2.XheW3Q.dGXK9j_ym9KOfkkKlVnM8olu5No"
game = discord.Game("Bot 개발중...")
loop = asyncio.get_event_loop()
@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(status = discord.Status.idle, activity=game)
    print("Running Bot...")

@client.event
async def on_message(message):

    help = Help()
    search = Search()
    now = datetime.datetime.now()

    if message.author.bot:
        return None
    
    #명령어 설명
    if message.content == "!명령어":
        createEmbed = help.create_help_embed()
        await message.channel.send(embed=createEmbed)

    #봇 설명
    if message.content == "!엣센스":
        createEmbed = help.Create_Bot_description()
        await message.channel.send(embed=createEmbed)


    if message.content == "!시간":
        await message.channel.send("현재 시각은 "+str(now.year)+"년 "+str(now.month),"월 "+str(now.day)+"일, "+str(now.hour)+"시 ",str(now.minute),"분 "+str(now.second)+"초 입니다.")


    if message.content == "!주사위":
        await message.channel.send(str(random.randint(1,6)))

    if message.content.startswith('!검색'):
        msg1 = message.content.split(' ')
        await message.channel.send(embed=search.search_image(msg1[1:]))


client.run(token)

