import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('hey boy use .help'))
    print('Bot is ready')

client.event
async def on_member_join(member):
    print(f'(member) has joined (server) aDDA')

@client.event
async def on_member_remove(member):
    print(f'(member) has left the (server)')

@client.command()
async def ping(ctx):
   await ctx.send(f'pong! {round(client.latency * 1000)}ms')

@client.command()
async def hp(ctx):
    await ctx.send('use .ping to test ur net')

@client.command()
async def load(ctx, extension):
    client.load_extension('cogs.{extention}')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
@client.command()
async def info(ctx):
    await ctx.send(' YOU ARE IN A PUBLIC SERVER ')

@client.command()
async def eliteace(ctx):
    await ctx.send(' https://www.youtube.com/channel/UC7tlGQXWt5HCRoZaugTDk9w?view_as=subscriber ')    

@client.command()
async def admin(ctx):
    embed = discord.Embed(
        title = 'ΞＬＩＴΞΛＣΣ',
        description = 'he is the admin of this server',
        colour = discord.Color.blue()
    )

    embed.set_footer(text='this is a footer')
    embed.set_image(url='https://images-ext-1.discordapp.net/external/FrhzDCUk9l7ErGM7YnhOl3tgfxQJyyTA5YvxOlBStcg/https/yt3.ggpht.com/a/AATXAJwAB1ZNqhmjyJm43n0YscF2H7ieAjQDhMN9KwKOcw%3Ds900-c-k-c0x00ffffff-no-rj?width=53&height=53')
    embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/FrhzDCUk9l7ErGM7YnhOl3tgfxQJyyTA5YvxOlBStcg/https/yt3.ggpht.com/a/AATXAJwAB1ZNqhmjyJm43n0YscF2H7ieAjQDhMN9KwKOcw%3Ds900-c-k-c0x00ffffff-no-rj?width=53&height=53')
    embed.set_author(name='ELITEACE',icon_url='https://images-ext-1.discordapp.net/external/FrhzDCUk9l7ErGM7YnhOl3tgfxQJyyTA5YvxOlBStcg/https/yt3.ggpht.com/a/AATXAJwAB1ZNqhmjyJm43n0YscF2H7ieAjQDhMN9KwKOcw%3Ds900-c-k-c0x00ffffff-no-rj?width=53&height=53')
    embed.add_field(name='permissons',value='Administrator', inline=False)
    embed.add_field(name='Roles',value='ㄚㄖㄩㄒㄩ乃乇尺丂,Admin', inline=False)
    embed.add_field(name='Available',value='1pm to 10pm', inline=True)
    
    await ctx.send(embed=embed)

client.run("NzYzNDE1MTg3OTM1OTg1NzA1.X33XzA.B-TQduNh9DaSYBVuvKioC3sf1Js")
