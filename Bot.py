import discord
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def 청소(ctx, amount=99):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

client.run('Njk2MjMzNTc3OTE4MTAzNTUy.XolwEQ._3kTRFVEbXcS8TIndG-KZFVFjVI')
