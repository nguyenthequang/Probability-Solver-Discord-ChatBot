import scipy
from scipy.stats import binom

#BASIC PROBS WITH 1 INPUT [Syntax: (# of trials, prob of success, # of successes)]
async def binomial_prob(ctx, n: int, p: float, x: int):
  if n < 0 or x < 0:
    await ctx.send("WARNING: # of trial and success shouldn't be negative")
  if x > n:
    await ctx.send("WARNING: # of success shouldn't be more than # of trials")
  if p > 1 or p < 0:
    await ctx.send("WARNING: probability should be within [0,1]")
    
  await ctx.send("Binomial(" + str(n) + ", " + str(p) + "), x = " + str(x))
  
  await ctx.send("pmf = f(x) = P[X = " + str(x) + "] = " + str(binom.pmf(x, n, p)))
  
  await ctx.send("cdf = F(x) = P[X <= " + str(x) + "] = " + str(binom.cdf(x, n, p)))

  await ctx.send("less than x = F(x - 1) = P[X < " + str(x) + "] = " + str(binom.cdf(x - 1, n, p)))
  
  await ctx.send("more than x = 1 - F(x) = P[X > " + str(x) + "] = " + str(1 - binom.cdf(x, n, p)))
  
  await ctx.send("at least x = 1 - F(x - 1) = P[X >= " + str(x) + "] = " + str(1 - binom.cdf(x - 1, n, p)))


#BASIC PROBS WITH 2 BOUNDS [Syntax: (# of trials, prob of success, lower bound, upper bound)]
async def binomial_bounds(ctx, n: int, p: float, x1: int, x2: int):
  if n < 0 or x1 < 0 or x2 < 0:
    await ctx.send("WARNING: # of trial and success shouldn't be negative")
  if x1 > n or x2 > n:
    await ctx.send("WARNING: # of success shouldn't be more than # of trials")
  if p > 1 or p < 0:
    await ctx.send("WARNING: probability should be within [0,1]")
  if x1 > x2 :
    await ctx.send("WARNING: lower bound (x1) should be less than higher bound (x2)")
  if x1 == x2:
    await binomial_prob(ctx, n, p, x1)
    return

  btw = binom.cdf(x2 - 1, n, p) - binom.cdf(x1, n, p)
    
  await ctx.send("Binomial(" + str(n) + ", " + str(p) + "), x1 = " + str(x1) + ", x2 = " + str(x2))
  
  await ctx.send("x between bounds = P[" + str(x1) + " < X < " + str(x2) + "] = " + str(btw))

  await ctx.send("x between bounds (inclusive) = P[" + str(x1) + " <= X <= " + str(x2) + "] = " + str(btw + binom.pmf(x2, n, p) + binom.pmf(x1, n, p)))


#CONFIDENCE INTERVAL [Syntax: (# of trials, prob of success, CI)]
async def binomial_ci(ctx, n: int, p: float, ci: float):
  if n < 0:
    await ctx.send("WARNING: # of trial shouldn't be negative")
  if ci > 1 or ci < 0:
    await ctx.send("WARNING: CI should be within [0,1]")
  if p > 1 or p < 0:
    await ctx.send("WARNING: probability should be within [0,1]")

  con_int = binom.interval(ci, n, p)
  percent = ci * 100

  await ctx.send("Binomial(" + str(n) + ", " + str(p) + ")")
  await ctx.send(str(percent) + "% CI = " + str(con_int))

#EXTRA INFO ABOUT DISTRIBUTION [Syntax: (# of trials, prob of success)]
async def binomial_extra(ctx, n: int, p: float):
  await ctx.send("Binomial(" + str(n) + ", " + str(p) + ")")
  await ctx.send("E[X] = mean = " + str(binom.mean(n, p)))
  await ctx.send("Median = " + str(binom.median(n, p)))
  await ctx.send("Var = " + str(binom.var(n, p)))