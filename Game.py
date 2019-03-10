# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:37:37 2019

@author: Tejinder Wadhwa
"""
#%%#
import pandas as pd
import numpy as np

class Players:
   
    word=""
    value=[]
    name=""
    score=0
    guess=[]
    choice=""
    in_word=''
    disp=list()
    
    def puzzle_start(self):
        print()
        self.display_str()
        ("==========================")
        print()
        print("Player: " +self.name+ "        Score: " +str(self.score))
        print()
        print("Would you like to:")
        print("1 Spin")
        print("2 Solve")
        self.choice = input('Enter 1 for Spin or 2 for Solve: ')
        self.chk_choice()
        print()
        print(*self.disp)
        return
    
    def chk_choice(self):
        if self.choice == '1' or self.choice == '2':
            if self.choice == '1':
                print("You choosed : Spin")
                print()
                self.spin()
            else:
                print("You choosed : Solve")
                self.solve()
                             
        elif self.choice !='1' and self.choice != '2':
                self.choice = input('Wrong Input!! Enter 1 for Spin or 2 for Solve: ')
                self.chk_choice()
        else:
            return

    
    def spin(self):
        i=0
        val = random.choice(self.value)
        print()
        print("Spin Value = $"+str(val))
        while (val != -1 and val != -2) and (self.disp.count('_') != 0):
            print("Your score = $"+str(self.score))
            print("Count of _ is "+str(self.disp.count('_')))
            print()
            self.in_word = input("Guess a letter: ")
            self.in_word = self.in_word.lower()
            print(self.in_word)
            if self.in_word in self.guess:
                print("Already Guessed!!! You loose your Turn")
                print("YOUR SCORE $"+str(self.score)+"!!!")
                break
            self.guess.append(self.in_word)
            print(self.guess)
            times=self.chk_input()
            self.score += (val*times)
            if (times == 0 or self.disp.count('_') == 0):
                break
            val = random.choice(self.value)
            print()
            print("Spin Value = $"+str(val))
            print("===================")
            
        if (val == -1):
            print()
            print("AHHHH!!! BANKRUPT!")
            print("YOU LOOSE YOUR TURN! YOUR SCORE RE-SET TO ZERO!!!")
            self.score=0
            print(self.score)
            print("===================")
            print("YOUR SCORE: $"+str(self.score))
        elif (val == -2):
            print()
            print("SORRY! YOU LOOSE YOUR TURN!")
            print("===================")
            print("YOUR SCORE: $"+str(self.score)+"!!!")
        elif self.disp.count('_') == 0:
            print()
            print("CONGRATULATIONS "+self.name+"!!!!")
            print("YOU GUESSED THE PUZZLE CORRECTLY!!!  YOU WON!!!")
            print("===================")
            print("YOUR FINAL SCORE: $"+str(self.score)+"!!!")

        else:
            return
                  


    def chk_input(self):
        print("In chk_input "+self.in_word)

        if (self.in_word in self.word) and (self.in_word != '') and (self.in_word != ' '):
            print("CORRECT GUESS!!!")
            self.display_str()
            print(self.in_word + " is there in  the word "+ str(self.word.count(self.in_word))+" times")
            return (self.word.count(self.in_word))
        else:
            print("SADLY!! IN-CORRECT GUESS!!!")
            print("YOU LOOSE YOUR TURN!!!")
            print("YOUR SCORE: $"+str(self.score)+"!!!")
            return 0
        

    def display_str(self):
        print("In display_str "+str(self.guess))
        disp_arr = np.asarray(self.disp)
        word_arr = np.asarray(list(self.word))
        for i in self.guess:
            c=0
            while (c < len(disp_arr)):
                if (i == word_arr[c]):
                    disp_arr[c] = word_arr[c]
                c=c+1
        print()
#        print(''.join(disp_arr.tolist()).title())            
        print(*disp_arr.tolist())            
        self.disp = disp_arr.tolist()
#        self.disp = ''.join(disp_arr.tolist()).title()
        return
        
    def solve(self):
        self.display_str()
        print("Guess the remaining "+str(self.disp.count('_'))+" letters!!!")
        val = random.choice(self.value)
        print()
        print("Spin Value = $"+str(val))
        self.in_word = input("Guess the word: ")
        if (self.in_word.lower() == self.word.lower()):
            self.score += ((self.disp.count('_'))*val)
            print()
            print("CONGRATULATIONS "+self.name+"!!!!")
            print("YOU GUESSED THE PUZZLE CORRECTLY!!!  YOU WON!!!")
            print("===================")
            print("YOUR FINAL SCORE: $"+str(self.score)+"!!!")
            self.disp = self.word
        else:
            print("IN-CORRECT GUESS!")
            print("YOU LOOSE YOUR TURN!")
            print("YOUR SCORE: $"+str(self.score)+"!!!")
       
        
        
    def show_underscore(self):
        i=0
        for x in self.word:
            if (x == " "):
                self.disp.append(x)
            else:
                self.disp.append("_")
            i=i+1
        print(*self.disp)
        return


    def chk_name(self):
        for x in self.name:
            if (x not in char) or (x ==''):
                print("Incorrrect entry!! Name can only have alphabets!!")
                self.name = input('Re-enter your name: ')
                self.chk_name()
            else:
                 continue

def random_puzzle(puzzles):
    return random.choice(puzzles)


def end_game():
    print()
    print("GAME ENDS!!! WORD GUESSED CORRECTLY!!")
    print("HERE ARE THE SCORES:")
    print("==========================================")
    print(player1.name+" SCORE = $"+str(player1.score))
    print(player2.name+" SCORE = $"+str(player2.score))
    print(player3.name+" SCORE = $"+str(player3.score))
    print("==========================================")
    return

game_values = pd.read_csv('D:\Game Challenge\wheel_values.txt',header = None)
game_values = game_values.iloc[:, 0].tolist()
print(game_values)

puzzles = pd.read_csv('D:\Game Challenge\wheel_puzzles.txt',header = None)
puzzles = puzzles.iloc[:, 0].tolist()
print(puzzles)

import random
word = random_puzzle(puzzles)
print(word)
type(word)

player1 = Players()
player2 = Players()
player3 = Players()

player1.word = player2.word = player3.word = word.lower()
player1.value = player2.value = player3.value = game_values
print(word)
print(player1.word)

print("WELCOME!!!!")
print("Guess the Word: ")
player1.show_underscore()
print()

char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

player1.name = input('Player 1 please enter your name: ')
player1.chk_name()
player2.name = input('Player 2 please enter your name: ')
player2.chk_name()
player3.name = input('Player 3 please enter your name: ')
player3.chk_name()

print()
print("Game Begins:")
 
cnt=1
while (player1.disp.count('_') !=0 and player2.disp.count('_') !=0 and player3.disp.count('_') !=0):
    if (player2.disp.count('_') !=0 and player3.disp.count('_') !=0):
        player1.disp = player3.disp
        print()
        print("ROUND "+str(cnt)+" BEGINS!!!!")
        print("=============================")
        player1.puzzle_start()
    if (player1.disp.count('_') !=0 and player3.disp.count('_') !=0):
        player2.disp = player1.disp
        player2.puzzle_start()
    if (player1.disp.count('_') !=0 and player2.disp.count('_') !=0):
        player3.disp = player2.disp
        player3.puzzle_start()
        cnt=cnt+1

end_game()
