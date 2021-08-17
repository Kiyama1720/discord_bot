import os
import datetime
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
  print('ログインしました')
  
@client.event
async def on_message(message):
  if message.author.bot:
    return
  
  if message.content == '/neko':
    await message.channel.send('にゃーん')
    
  if message.content == '/today':
    dt_now = datetime.datetime.now() 
    dt_now = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
    await message.channel.send(dt_now)
  
client.run(TOKEN)