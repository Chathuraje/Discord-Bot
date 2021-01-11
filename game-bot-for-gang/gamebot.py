import discord
import random
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='//')
client = discord.Client()
TOKEN = '' # Replce your Discod Token

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def guess (ctx, guess):
    
    hidden = random.randrange(1,10)
    guess =  int (guess)
    if guess == hidden:
        if ctx.author.id == "650394026822074389":
            await ctx.send("you are great jiri :smiley:")
        else:
            await ctx.send("you are great " +str(ctx.author.display_name)+ " :smiley:")
    elif guess < hidden:
        await ctx.send("your guess is to low")  
    elif guess > hidden:
        await ctx.send("your guess in too high")
    
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def hi(ctx):
    if ctx.author.id == '650394026822074389':
        await ctx.send(":smiley: :wave: Hello, jiri")
    else:
        await ctx.send(":smiley: :wave: Hello, " +str(ctx.author.display_name))
        
@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

#hangman
guesses = ''

text_file = open('words.txt', 'r')

words = text_file.read().split('\n')

#words = ["aaa"]

word = ""

wordpos = random.randrange(0,len(words))
word = words[wordpos]

@bot.command()
async def hgman_new(ctx):
    
    global guesses
    global word
    
    guesses = ''
    wordpos = random.randrange(0,len(words))
    word = words[wordpos]

    letter = " "
    count = 0
    embed = discord.Embed(title="World is: ", description="", color=0xeee657)
    for char in word:
        count += 1
        if (char == letter):
            embed.add_field(name=count, value=char)
            guesses += char
        else:
            if char in guesses:
                embed.add_field(name=count, value=char)
            else:
                embed.add_field(name=count, value="_")
                
    await ctx.send(embed=embed)


@bot.command()
async def hgman_view(ctx):
    
    global guesses
    global word

    letter = " "
    count = 0
    embed = discord.Embed(title="World is: ", description="", color=0xeee657)
    for char in word:
        count += 1
        if (char == letter):
            embed.add_field(name=count, value=char)
            guesses += char
        else:
            if char in guesses:
                embed.add_field(name=count, value=char)
            else:
                embed.add_field(name=count, value="_")
                
    await ctx.send(embed=embed)
    
    
@bot.command()
async def hgman(ctx, letter):

    global guesses
    global word

    g = 0
    count = 0

    if letter in guesses:
        await ctx.send("Alrady Guessed!!")
        g = 1
                
    if letter not in word:
        await ctx.send("Wrong Guess!!")
    
    embed = discord.Embed(title="World is: ", description="", color=0xeee657)
    for char in word:
        count += 1
        if (char == letter):
            embed.add_field(name=count, value=char)
            if (g == 0):
                guesses += char
        else:
            if char in guesses:
                embed.add_field(name=count, value=char)
            else:
                embed.add_field(name=count, value="_")
        
    await ctx.send(embed=embed)

    if (len(word) == len(guesses)):
        await ctx.send("Won!!")
        await ctx.send("Word is: " + word)
        guesses = ""

        await ctx.send("Starting New game")
        
        wordpos = random.randrange(0,len(words))
        word = words[wordpos]

        letter = " "
        count = 0
        embed = discord.Embed(title="World is: ", description="", color=0xeee657)
        for char in word:
            count += 1
            if (char == letter):
                embed.add_field(name=count, value=char)
                guesses += char
            else:
                if char in guesses:
                    embed.add_field(name=count, value=char)
                else:
                    embed.add_field(name=count, value="_")
                
        await ctx.send(embed=embed)


#remove help
bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="**game bot commands**", description="this commands help you to get the commands easily", color=0xeee657)

    embed.add_field(name="**//hi**", value="say HI to bot", inline=False)
    embed.add_field(name="**//guess**", value="guess game", inline=False)

    embed.add_field(name="**//hgman <letter>**", value="hangman game", inline=False)
    embed.add_field(name="**//hgman_view**", value="view current hangman game", inline=False)
    embed.add_field(name="**//hgman_new**", value="restart hangman game", inline=False)

    embed.add_field(name="**//add**", value="to add numbers", inline=False)

    embed.add_field(name="**//multi**", value="to multiply numbers", inline=False)

    embed.add_field(name="**//cat**", value="just for fun", inline=False)

    embed.add_field(name="**//help**", value="show this message", inline=False)
   
    await ctx.send(embed=embed)


bot.run(TOKEN)


