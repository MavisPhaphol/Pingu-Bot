import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content

bot = commands.Bot(command_prefix="$", intents=intents)

#made by Mavis Phaphol
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "lizard" in message.content.lower(): #lizard without the syntax
        lizardMeme="https://tenor.com/view/lizard-gif-4323854089874490655"
        await message.channel.send(lizardMeme)
    ##SEPARATE FROM IF
    await bot.process_commands(message)

#made by Mavis Phaphol
@bot.command() #test command to ensure functionality
async def test(ctx):
    await ctx.send("Test Successful")

#made by Mavis Phaphol
@bot.command() #heads or tails command
async def ht(ctx,choice:str):
    userChoice=choice.lower()
    flip=random.choice(["heads","tails"])
    await ctx.send("Your Choice: "+userChoice+"\nResults: "+flip)

#made by Mavis Phaphol
@bot.command() #Random Selection command
async def choose(ctx,choices:str):
    options=choices.split()
    randomSelection=random.choice(options)
    await ctx.send("**PINGU SELECTS**: "+randomSelection)

#made by Mallory Phaphol
@bot.command() #Rock Paper Scissor command
async def rps(ctx,choices:str):
    userChoice=choices.lower()
    shoot=random.choice(["rock","paper","scissors"])
    await ctx.send("Your pick: "+userChoice+"\nPingu pick: "+shoot)
    if userChoice==shoot:
        await ctx.send("Tie!")
    elif (
        (userChoice=="rock" and shoot=="scissors") or
        (userChoice=="scissors" and shoot=="paper") or
        (userChoice=="paper" and shoot=="rock") ):
            await ctx.send("You win!")
    else:
        await ctx.send("Pingu win!")

#made by Mallory Phaphol
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "pingu" in message.content.lower():
        pinguWaddle="https://tenor.com/view/catscafe-penguin-run-mood-gotta-go-gif-15488237"
        await message.channel.send(pinguWaddle)
    await bot.process_commands(message)

bot.run("*BOT TOKEN*")




