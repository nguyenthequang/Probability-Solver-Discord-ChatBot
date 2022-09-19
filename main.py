from discord.ext import commands
import discord
import os
import random

from binomial import *
from multinomial import *

bot = commands.Bot(command_prefix='!')

#_________________________EXTRA STUFF________________________________

bot.videos = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://www.youtube.com/watch?v=yPYZpwSpKmA", "https://www.youtube.com/watch?v=wCN9WliV-ew", "https://www.youtube.com/watch?v=PWbRleMGagU", "https://www.youtube.com/watch?v=8McISUEXb9g"]


@bot.command(help = "Say hi to user")
async def hello(ctx):
    await ctx.send("hello " + ctx.author.display_name)


@bot.command(help = "Get random music in the list")
async def random_music(ctx):
    picked = random.choice(bot.videos)
    if picked == "https://www.youtube.com/watch?v=dQw4w9WgXcQ":
      await ctx.send("You Just Got RICK ROLLED!!!")
    await ctx.send(picked)

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

#________________________MULTINOMIAL DIS_____________________________
      
@bot.command(help = "Multi: basic prob with an arr of # of occurence of xi, and an arr of prob of xi's")
async def multi_prob(ctx, xi, pi):
  await multinomial_prob(ctx, xi, pi)

@bot.command(help = "Multi: extra info")
async def multi_extra(ctx):
  await multinomial_extra(ctx)

#Prevent too many request error (429)
try:
    password = os.environ['password']
    bot.run(password)
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    system("python restarter.py")
    system('kill 1')