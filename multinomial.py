import scipy
import numpy as np

from scipy.stats import multinomial

#BASIC PROBS WITH 2 ARRAYS [Syntax: (list of # of xi's, list of prob for each xi's)]
async def multinomial_prob(ctx, xi, pi):
  x_arr = np.array([])
  p_arr = np.array([])
  
  #Process the list of Xi's and make the str version for printing
  x_list = xi.split(",")
  for x in x_list:
    x_arr = np.append(x_arr, int(x))
  x_str = ', '.join(str(x) for x in x_arr)
    
  #Process the list of probability and make the str version for printing
  p_list = pi.split(",")
  for p in p_list:
    p_arr = np.append(p_arr, float(p))
  p_str = ', '.join(str(p) for p in p_arr)
  
  n = int(sum(x_arr))

  multi = multinomial.pmf(x_arr, n, p_arr)
  
    
  await ctx.send("Multinomial(" + str(n) + ", " + p_str + ")")
  
  await ctx.send("pmf = f(x) = P[Xi's = " + x_str + "] = " + str(multi))
  
  await ctx.send("Explanation: For " + str(n) + " trials, this is the probability that X1 = " + str(x_arr[0]) + ", X2 = " + str(x_arr[1]) + ", etc.")


#EXTRA INFO ABOUT DISTRIBUTION [Syntax: (# of trials, prob of success)]
async def multinomial_extra(ctx):
  await ctx.send("E[Xi] = mean of xi = n * pi")
  await ctx.send("Var[Xi] = n * pi(1 - pi)")