from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}금천구를 소개해줘':
        await message.channel.send("금천구는 개발중인 로블록스 KR:RP형태의 서버입니다.")

    if message.content.startswith(f'{PREFIX}안녕하세요!'):
        await message.channel.send('금천구에 오신걸 환영합니다!')
        
@bot.event
async def on_member_join(member):
    await member.guild.get_channel(1069624743944278179).send(member.mention + "님! 여기는 서울특별시 금천구 입니다. 환영합니다!")
    return

@bot.event
async def on_member_remove(member):
    await member.guild.get_channel(1078978489836896318).send(member.mention + "님, 서울특별시 금천구 였습니다. 안녕히가십시오!")
    return


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
