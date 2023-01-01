# Probability-Solver-Discord-ChatBot
A simple Discord chatbot that can solve simple probability problems

This project ultilizes my knowlegde of Discord Chatbot and my statistics knowledge.
The main points of this project is to create something that can cut down the calculation required to solve a probability problem.

There are a lot of different websites that do these type of stuff already, but most of them only cover 1 distribution. This chatbot will cover mostly the basics, but it will be more generallized, i.e. you can do many distributions on here without jumping through many sites.

Aside from few random commands, most stats-related commands follow a common format.

In your Discord's chat, type: !distribution_function parameters (Ex: !binom_prob 10 0.5 4).
Alternatively, you can type !help to view all possible commands.

*available distribution is binom, multinomial, norm.

function usually includes: 

                           prob(calculate multiple simple probs like F(X = 4)),

                           ci(confident interval for true means),
                           
                           extra(give E[X], Var, SD, etc.)
