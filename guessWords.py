import random

def GuessWords():  chances=0 
    fileName = input("Enter you guess: ") number = random.randint(1, 9)
while chances < 5:
    guess = input("Enter you guess: ")
        if guess == number: 
    print("Congratulations you won!!!")

    chances +=1 


     if chances >=5:
       print("You lose!!! The number is", number) 

       GuessWords() 