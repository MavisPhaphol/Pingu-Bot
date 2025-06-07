import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.command()
async def test(ctx):
    await ctx.send("Test Successful")

@bot.command()
async def ht(ctx,choice:str):
    choice=choice.lower()
    flip=random.choices(["heads","tails"])


bot.run("*BOT TOKEN*")
