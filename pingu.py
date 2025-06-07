import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.command()
async def test(ctx):
    await ctx.send("Test Successful")



bot.run("*BOT TOKEN*")