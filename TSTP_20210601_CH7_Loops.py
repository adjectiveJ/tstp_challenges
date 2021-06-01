"""
The Self-Taught Programmer - Chapter 7 Loops
Author: Dante Valentine
Date: 1 June, 2021
"""

# CHALLENGE 1 (print shows from a list)
list1 = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for show in list1:
    print(show)

# CHALLENGE 2 (print all numbers from 25 to 50)
for i in range(25,51):
    print(i)

# CHALLENGE 3A (print shows from the list as well as their index)
i = 0
for show in list1:
    print(show + " " + str(i))
    i +=1

# CHALLENGE 3B (print shows from the list as well as their index, but with enumerate)
for i, show in enumerate(list1):
    print(show, i)

# CHALLENGE 4 (write a program with an infinite loop [with option to quit] and a list of numbers. each time through the loop, ask user to guess a number from the list and tell whether they guessed correctly)
numberlist = [3, 11, 27, 30, 90, 94]
while True:
    print("Type q to quit")
    guess = input("Guess a number from 1 to 100: ")
    if guess == "q":
        break
    if int(guess) in numberlist:
        print("Correct! " + guess + " is in the list.\n")
    else:
        print("Try again!\n-----\n")
print("Good game!\n")

# CHALLENGE 5 (multiply all numbers in given list with all numbers in second given list and append results to a new third list")
list2 = [8, 19, 148, 4]
list3 = [9, 1, 33, 83]
list4 = []
for i in list2:
    for j in list3:
        newint = i*j
        list4.append(newint)
print(list4)