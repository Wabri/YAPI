# Rice Bot by Ian Duncan
import discord
import random
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from flickrapi import FlickrAPI
import json

FLICKR_PUBLIC = 'ca6684ea55ea6286873b5ec7538373f2'
FLICKR_SECRET = '6cd093499b7a9271'
DISCORD_TOKEN = 'NDg2MjgyMTU3NTgxNDAyMTEz.DwRt5A.tXxnekJ032XzalP5l9XBhQVxQ0M'

bot = commands.Bot(command_prefix='#')
flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='json')
photo_urls1 = []
photo_titles1 = []
extras='url_c,url_o'
query_term1 = 'rice Field'

@bot.event
async def on_ready():
    print("Rice Bot Ready!")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pinged successfully!")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title=f"{user.name}'s info", description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name=f"{ctx.message.server.name}'s info", description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def update(user: discord.Member, perpage = 1000):
    global photo_urls1
    global photo_titles1
    print("Updating Ricefields")
    photo_urls1.clear()
    photo_titles1.clear()
    #flickrapi
    fields = flickr.photos.search(text=query_term1, per_page=perpage, extras=extras)
    photos = json.loads(fields)
    for index in range(len(photos['photos']['photo'])):
        if 'url_c' in photos['photos']['photo'][index]:
            if 'title' in photos['photos']['photo'][index]:
                photo_urls1.append(photos['photos']['photo'][index]['url_c'])
                photo_titles1.append(photos['photos']['photo'][index]['title'])
    embed = discord.Embed(title='Updating Rice Field List', color=0x00ff00)
    embed.add_field(name="Images Found", value=len(photo_urls1))
    await bot.saw(embed=embed)

@bot.command(pass_context=True)
async def riceField(user: discord.Member):
    global photo_urls1
    global photo_titles1
    number = random.randrange(0, len(photo_urls1))
    url = photo_urls1[number]
    title = photo_titles1[number]
    embed = discord.Embed(title=f'{title}', description='A random rice field', color=0x00ff00)
    embed.set_image(url=url)
    embed.set_footer(text=f'Image #{number}')
    print(f'Image #{number}')
    await bot.say(embed=embed)

bot.run(DISCORD_TOKEN)
