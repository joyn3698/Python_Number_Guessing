""" This is one of my first projects made after I learned OOP. This is a number guessing game but with something more. Here, you can choose the number of attempts you 
want to finish the game and also you can choose any range of number, beginning being 1. """
import random

class Guess():
    def __init__(self):
        self.tries=0
                        
    def game(self):
        self.attempts=int(input("Enter the number of attempts you want for guessing the number: "))          #input your choice of attempts
        self.range_of_numbers=int(input("Enter the highest number you want to for the range of numbers: "))  #input the highest number for the range of numbers to guess
        self.random=random.randint(1,self.range_of_numbers)
        while True:

            if self.attempts>0:
                self.user_choice=int(input("\nGuess the number: "))
                if self.user_choice>self.random:
                    print("\nYour guess is too high")
                    self.attempts-=1                                                                         #attempt decreases by each guess
                    self.tries+=1                                                                            #tries increases by 1
                    print("You have "+str(self.attempts)+" attempts left")
                elif self.user_choice<self.random:
                    print("\nYour guess is too low")
                    self.attempts-=1
                    self.tries+=1
                    print("You have "+str(self.attempts)+" attempts left")
                elif self.user_choice==self.random:
                    self.tries=self.tries+1
                    print("\nYou guessed it correctly in "+str(self.tries)+" tries")
                    break
            else:
                print("You lose")
                break
            
new_game=Guess()
new_game.game()




        