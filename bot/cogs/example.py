#importing modules........
import discord
from discord.ext import commands

#making classess..........
class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

#EVENTs
    @commands.Cog.listener()
    async def on_ready(self):
        print('COG activated')


#cog commands
    @commands.command()
    async def hi(self, ctx):
        await ctx.send('HELLO')

def setup(client):
    client.add_cog(Example(client))
