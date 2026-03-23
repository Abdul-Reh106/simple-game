import random 

print("NUMBER GUESSING GAME!!! ")
print("Think of a number between 1 and 100.")
print("You've 5 attempts to guess the number. ")

num_to_guess = random.randint(1, 100)
atmps = 5 

for atmp in range(1,atmps+1):
    print(f"\n{atmp} attempt out of {atmps}\n")
    
    try:
        guess = int(input("Guess the number-> "))
        if guess <1 or guess >100:
            print("Number should be guess between 1 and 100. ")
            continue
        if guess == num_to_guess :
            print("Congratulations!!! You Won The Game.")
            print(f"You take {atmp} attempts. ")
            break
        
        diff = num_to_guess - guess
        
        if abs(diff) <= 10:
            if abs(diff)<=5:
                if diff>0:
                    print("SO CLOSE !!.\nA LITTLE HIGHER..")
                else:
                    print("SO CLOSE !!.\nA LITTLE LOWER..")
            else:
                if diff>0:
                    print("CLOSE!!.\nTRY A BIT HIGHER ")
                else:
                    print("CLOSE!!.\nTRY A BIT LOWER")
        else:
            if diff> 0:
                print("Too low")
            else:
                print("Too high")    
        if atmp == atmps :
            print(f"OOPSS GAME OVER!! \nThe number was {num_to_guess}. ")
    
    except ValueError:
        print("Please enter the valid number")
        continue 