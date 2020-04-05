import discord
import random
import os
from discord.ext import commands
import datetime

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('Bot is ready')
@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("Chat Moritoring")
    await client.change_presence(status=discord.Status.online, activity=game)
 
@client.command()
async def 청소(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)


access_token = os.environ["BOT_TOKEN"]  
client.run(access_token)
