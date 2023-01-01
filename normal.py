import scipy
from scipy.stats import norm
import numpy as np

async def normal_prob(ctx, x: float, mean: float, sd: float):
  dis = "N(" + str(mean) + ", " + str(sd) + "^2)"

  await ctx.send("pdf = f(x) = P[X = " + str(x) + "] = " + str(norm.pdf(x, mean, sd)))
  
  await ctx.send("cdf = F(x) = left tail = P[X <= " + str(x) + "] = " + str(norm.cdf(x, mean, sd)))

  await ctx.send("1 - F(x) = right tail = P[X > " + str(x) + "] = " + str(1 - norm.cdf(x, mean, sd)))

  await ctx.send("Z-score of " + str(x) + " = (x-mean)/sd = " + str((x - mean) / sd))

async def normal_extra(ctx):
  await ctx.send("A normal distribution is determined by its mean and variance")
  await ctx.send("Var[X] = sd^2")
  await ctx.send("Normal Dis is symmetric: P(X > c) = P(X < -c)")
  