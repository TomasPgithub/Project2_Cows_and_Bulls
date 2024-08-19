"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

autor: Tomáš Plechatý
email: tomplechaty@seznam.cz
discord: Gulas_D_Kom#9800
"""
import time
import random


    
def intro():
    """Vypíše úvodní pozdrav a vyzve ke hře"""
    print("Hi There!")
    print(47*"-")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(47*"-")

def generate_random_number():
    """Vytvoří náhodné číslo s unikátními číslicemi nezačínající na nulu"""
    first,second,third,fourth = None, None, None, None
    #reset obsahu proměnných před novou generací čísla
    pool = {1,2,3,4,5,6,7,8,9}
    first = str(random.choice(list(pool)))
    #print(first)
    pool.add(0)
    pool.remove(int(first))
    #print(pool)
    second = str(random.choice(list(pool)))
    pool.remove(int(second))
    #print(second)
    #print(pool)
    third = str(random.choice(list(pool)))
    pool.remove(int(third))
    #print(third)
    #print(pool)
    fourth = str(random.choice(list(pool)))
    pool.remove(int(fourth))
    #print(fourth)
    #print(pool)
    random_number = first+second+third+fourth
    return random_number
    
def input_control(string_of_numbers:str):
    """Kontrola, zda číslo na vstupu neobsahuje jiný počet cifer než 4,
    zda neobsahuje nečíselné znaky, zda nezačíná na 0 , či zda neobsahuje duplicity"""
    first_char = string_of_numbers[0]
        
    if len(string_of_numbers) != 4:
        print("Zadej čtyřmístné číslo")
        return False    
        
    elif first_char == "0":
        print("Číslo nesmí začínat nulou")
        return False
    
    elif not string_of_numbers.isnumeric():
        print("Číslo nesmí obshaovat nečíselné znaky")    
        return False
        
    elif len(set(string_of_numbers)) != len(string_of_numbers):
        print("Číslo nesmí obsahovat duplicity")
        return False

    elif string_of_numbers.isdigit() and first_char != "0" and len(string_of_numbers) == 4:
        return True 
    
def count_bulls_and_cows(guess,random_number):
    
    bulls = 0
    cows = 0
    for digit in range(len(guess)):
        #print(" srovnávám čísla ", guess[digit],"a ", random_number[digit]," z ", guess," a ", random_number)   #pro debug
        if random_number[digit] == guess[digit]:
            bulls+=1
            #print("býk přidán)")                       #pro debug
        elif guess[digit] in random_number: 
            cows+=1
            #print(guess[digit], "je v ", random_number)        #pro debug
            #print("cow pridana")                               #pro debug
    return bulls, cows

def evaluation(bulls,cows):
    """Vypíše počet Býků a Krav ve správném tvaru jednotného nebo množného čísla"""
    plural1 = ""
    plural2 = ""
    if bulls != 1:
        plural1 = "s"
    if cows != 1:
        plural2 = "s"
    print(bulls," bull",plural1," ", cows, " cow",plural2, sep="")
    return 

def guess_call():
    print("Enter a number:")
    print(47*"-")
    guess = str(input())
    return guess

def gratulation_stats_and_end(attempt):
    """Oznámení vítězství, výpis počtu potřebných pokusů a spotřebovaný čas."""
    attempt+=1
    print("Correct, you've guessed the right number")
    print("in ",attempt, "guesses!")
    print(47*"-")
    time = end - start
    print("Your time was ",time//360,"h ", (time%360)//60,"min ", time%60,"sec"  )
    


intro()
random_number = generate_random_number()
#print (random_number) #pro kontrolu
start = time.time() #spustí stopky
guess = guess_call()
attempt = 0 # nastaví počítadlo pokusů

while guess != random_number:
    if not input_control(guess):
        guess = guess_call()
        continue
    bulls, cows = count_bulls_and_cows(guess,random_number)
    evaluation(bulls,cows)
    attempt +=1 # přičte pokus
    guess = guess_call()
        
end = time.time() #zastaví stopky
gratulation_stats_and_end(attempt)


