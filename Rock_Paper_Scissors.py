#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random


# In[3]:


#rock paper scissors game
select = ['Rock', 'Paper', 'Scissors']
player = False
player_score = 0
cpu_score = 0
while True:
    computer = random.choice(select)
    player = input("Rock, Paper or Scissors? (or 'End'): ").capitalize()
    
    if player == computer:
        print("Tie")
    elif player == 'Rock':
        if computer == 'Paper':
            print("You lose", computer, "covers", player)
            cpu_score +=1
        else:
            print("you win", player, "smash", computer)
            player_score +=1
    elif player == 'Paper':
        if computer == 'Scissors':
            print("you lose", computer, "cuts", player)
            cpu_score +=1
        else:
            print("you win", player, "covers", computer)
            player_score +=1
    elif player == 'Scissors':
        if computer == 'Rock':
            print("you lose", computer, "smash", player)
            cpu_score +=1
        else:
            print("you win", player, "cuts", computer)
            player_score +=1
    elif player == 'End':
        print("Final score:")
        print(f"computer score is {cpu_score}")
        print(f"player score is {player_score}")
        break
    else:
        print("play again")


# In[ ]:





# In[ ]:





# In[ ]:




