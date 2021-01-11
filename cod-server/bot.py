import discord
from discord.ext import commands
import random

TOKEN = '' # Replce your Discod Token
bot = commands.Bot(command_prefix='+')

#On Ready
@bot.event
async def on_ready():
    print('Logged in as ' + str(bot.user.name) + ": " + str(bot.user.id))

#Greeting
@bot.command()
async def greet(ctx):
    embed = discord.Embed(title="Welcome to Discord", description=":smiley: :wave: Hello, there!", color=0xeee657)
    await ctx.send(embed=embed)
        
#Guess
@bot.command()
async def guess(ctx, guess):
    hidden = random.randrange(1,20)
    guess = int(guess)
    if guess == hidden:
        await ctx.send("great")
    elif guess < hidden:
        await ctx.send("your guess is to low")
    elif guess > hidden:
        await ctx.send("your guess in too high")
                 
@bot.command()
async def cat(ctx):
    await ctx.send('https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif')
    
#Info
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="COD-SERVER Information ", description="Bot for the cod-server", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="Chathura J Ekanayake")
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    await ctx.send(embed=embed)

#Server IP
@bot.command()
async def ip(ctx):
    embed = discord.Embed(title="Cod-Server IP", description="/connect 182.161.20.241:28963; password 1234", color=0xeee657)

    await ctx.send(embed=embed)

#Install
@bot.command()
async def install(ctx):
    embed = discord.Embed(title="Installation Instruction", description="https://cod4x.me/index.php?/forums/topic/12-how-to-install-cod4x/", color=0xeee657)
    
    await ctx.send(embed=embed)

#Status
@bot.command()
async def status(ctx):
    embed = discord.Embed(title="Status", description="Online", color=0xeee657, delete_after=5)
    
    await ctx.send(embed=embed)

#Clear///////////
@bot.command(pass_context=True)
async def clear(ctx):
    await ctx.message.delete()
    embed = discord.Embed(description="Action completed! :smile:", color=0x00ff00)
    await ctx.send(embed=embed)



#Help
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Cod Bot Help", description="A cod-server bot. List of commands are:", color=0xeee657)

    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$ip", value="Gives a IP address of Server", inline=False)
    embed.add_field(name="$install", value="Gives a Client installation details", inline=False)
    embed.add_field(name="$status", value="Gives a Server Status", inline=False)
    embed.add_field(name="$clear", value="Clear all bot messages", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run(TOKEN)

