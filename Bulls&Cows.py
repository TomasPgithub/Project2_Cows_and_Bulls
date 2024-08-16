"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

autor: Tomáš Plechatý
email: tomplechaty@seznam.cz
discord: Gulas_D_Kom#9800
"""
import time
import random

def start_timer():
    start = time.time()
    return start

def end_timer():
    end = time.time()
    return end    
    
def intro():
    print("Hi There!")
    print(47*"-")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(47*"-")

def generate_random_number():
    first = random.randint(1,9)
    second = random.randint(0,9)
    while second == first:
        second = random.randint(0,9)
    third = random.randint(0,9)
    while third == first or third == second:
        third = random.randint(0,9)
    fourth = random.randint(0,9)
    while fourth == first or fourth == second or fourth == third:
        fourth = random.randint(0,9)
    first_str = str(first)
    second_str = str(second)
    third_str = str(third)
    fourth_str = str(fourth)
    random_number = first_str+second_str+third_str+fourth_str
    return random_number
    #V případě generace delšího unikátního čísla bych vybíral náhodné prvky z  množiny čísel 0-9 a vybrané prvky pak odebíral z množiny. 



    
def input_control(string_of_numbers):
    first_char = string_of_numbers[0]
        
    if len(string_of_numbers) != 4:
        print("Zadej čtyřmístné číslo")
        return False    
        
    elif first_char == "0":
        print("Číslo nesmí začínat nulou")
        return False
    
    elif not string_of_numbers.isnumeric():
        print("Číslo obsahuje nečíselné znaky")    
        return False
        
    elif find_repeating_digits(string_of_numbers):
        print("Číslo nesmí obsahovat duplicity")
        return False

    elif string_of_numbers.isdigit() and first_char != "0" and len(string_of_numbers) == 4:
        return True
        
def find_repeating_digits(num):
    
    str_num = str(num)  
    if len(set(str_num)) != len(str_num):
        print("duplicita")
        return True
    else:
        return False    
    
def count_Bulls_and_Cows(guess,random_number):
    
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


def set_counter():
    attempt = 0
    return attempt

def add_counter(attempt):
    attempt+=1
    return attempt

def evaluation(bulls,cows):
    if bulls == 1 and cows == 1:
        print(bulls,"bull, ", cows, "cow")
        return 
    if bulls == 1 and cows != 1:
        print(bulls,"bull, ", cows, "cows")
        return 
    if bulls != 1 and cows == 1:
        print(bulls,"bulls, ", cows, "cow")
        return     
    if bulls != 1 and cows != 1: 
        print(bulls,"bulls, ", cows, "cows")
        return 
    
def get_stats():
    pass

def save_stats():
    time = end - start
    pass

def calculate():
    time = end-start
    return time
    pass

def guess_call():
    print("Enter a number:")
    print(47*"-")
    guess = str(input())
    return guess

def gratulation_stats_and_end(attempt):
    attempt+=1
    print("Correct, you've guessed the right number")
    print("in ",attempt, "guesses!")
    print(47*"-")
    get_stats()
    time = calculate()
    print("Your time was ",time//360,"h ", (time%360)//60,"min ", time%60,"sec"  )
    save_stats()





intro()
random_number = generate_random_number()
#print (random_number) #pro kontrolu
start = start_timer()
guess = guess_call()
attempt = set_counter()

while guess != random_number:
    if not input_control(guess):
        guess = guess_call()
        continue
    bulls, cows = count_Bulls_and_Cows(guess,random_number)
    evaluation(bulls,cows)
    attempt = add_counter(attempt)
    guess = guess_call()
        
end = end_timer()
gratulation_stats_and_end(attempt)


