# List of modules I have imported

import random

# List of animes that I may want to watch in the future
# Note the order is name, genre, length and type

animes = [['bleach' , 'shonen' , 'long' , 'series'] ,
          ['monster' , 'thriller' , 'medium' , 'series'] ,
          ['mob psycho' , 'comedy' , 'medium' , 'series'] ,
          ['hajime no ippo' , 'sports' , 'long' , 'series'] ,
          ['samurai champloo' , 'adventure' , 'short' , 'series'],
          ['perfect blue' , 'thriller' , 'short' , 'movie'],
          ['my neighbor totoro' , 'adventure' , 'short' , 'movie'],
          ['spirited away' , 'adventure' , 'short' , 'movie'],
          ['princess mononoke' , 'adventure' , 'short' , 'movie']]

Genre = input('What type of anime are you feeling right now? (Type "any" if you have no preference): ').lower()
Type = input('Do you want to watch a "series" or a "movie? (Type "any" if you have no preference): ').lower()
Length = input('Do you want a short, medium or long anime? (Type "any" if you have no preference): ').lower()


# Incase multiple suggestions are valid, they will enter this list and then be randomised
Valid =[]



for item in animes:
        if (item[1] == Genre or Genre == 'any') and \
           (item[2] == Length or Length == 'any') and \
           (item[3] == Type or Type == 'any'):
           Valid.append(item)
        
           
if Valid:
      suggest = random.choice(Valid)
      print(f'I would reccomend the {suggest[2]} {suggest[3]} {suggest[1]} anime: {suggest[0].title()}')
           

        
else:
      print("Sorry, I do not have any reccomendations")
