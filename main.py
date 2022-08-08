from discord.ext import commands
import os
import random

from binomial import *

#_________________________EXTRA STUFF________________________________

bot = commands.Bot(command_prefix='!')
bot.videos = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://www.youtube.com/watch?v=yPYZpwSpKmA", "https://www.youtube.com/watch?v=wCN9WliV-ew", "https://www.youtube.com/watch?v=PWbRleMGagU", "https://www.youtube.com/watch?v=8McISUEXb9g"]

bot.happylist = ["Cat", "Dog", "Games"]

@bot.command(help = "Say hi to user")
async def hello(ctx):
    await ctx.send("hello " + ctx.author.display_name)


@bot.command(help = "Get random music in the list")
async def random_music(ctx):
    picked = random.choice(bot.videos)
    if picked == "https://www.youtube.com/watch?v=dQw4w9WgXcQ":
      await ctx.send("You Just Got RICK ROLLED!!!")
    await ctx.send(picked)


@bot.command(help = "Note 1 item that make you happy")
async def happy(ctx, item):
    await ctx.send("Awesome!")
    bot.happylist.append(item)
    print(bot.happylist)


@bot.command(help = "Give you 1 happy item")
async def sad(ctx):
  await ctx.send("Hope this makes you feel better!")
  await ctx.send(random.choice(bot.happylist))


@bot.command(help = "Simple calculator")
async def calc(ctx, x: float, fn: str, y: float):
    if fn == '+':
        await ctx.send(x + y)
    elif fn == '-':
        await ctx.send(x - y)
    elif fn == '*':
        await ctx.send(x * y)
    elif fn == '/':
        await ctx.send(x / y)
    else:
        await ctx.send("We only support 4 function operations")

      

#_________________________BINOMIAL DIS_______________________________
      
@bot.command(help = "Binom: basic prob with 1 input (x)")
async def binom_prob(ctx, n: int, p: float, x: int):
  await binomial_prob(ctx, n, p, x)

@bot.command(help = "Binom: prob between 2 bounds x1 and x2")
async def binom_bounds(ctx, n: int, p: float, x1: int, x2: int):
  await binomial_bounds(ctx, n, p, x1, x2)

@bot.command(help = "Binom: confident interval for true mean (p is for sample prob)")
async def binom_ci(ctx, n: int, p: float, ci: float):
  await binomial_ci(ctx, n, p, ci)

@bot.command(help = "Binom: extra info")
async def binom_extra(ctx, n: int, p: float):
  await binomial_extra(ctx, n, p)
  
password = os.environ['password']
bot.run(password)