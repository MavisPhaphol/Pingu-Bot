import random

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event #ADDED
async def on_message(message): #ADDED
    if message.author == bot.user:
        return
    if "lizard" in message.content.lower(): #lizard without the syntax
        lizardMeme="https://tenor.com/view/lizard-gif-4323854089874490655"
        await message.channel.send(lizardMeme)
    ##SEPARATE FROM IF
    await bot.process_commands(message)

@bot.command() #test command to ensure functionality
async def test(ctx): #ADDED
    await ctx.send("Test Successful")

@bot.command()
async def ht(ctx,choice:str): #heads or tails command
    userChoice=choice.lower() #ADDED
    flip=random.choice(["heads","tails"])
    await ctx.send("Your Choice: "+userChoice+"\nResults: "+flip)

@bot.command() #Random Selection command
async def choose(ctx,choices:str): #ADDED
    options=choices.split()
    randomSelection=random.choice(options)
    await ctx.send("**PINGU SELECTS**: "+randomSelection)

bot.run("**BOT TOKEN**") #bot goes online (will terminate when the file stops running)

