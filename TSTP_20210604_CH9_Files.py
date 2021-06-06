"""
The Self-Taught Programmer - Chapter 8 Files
Author: Dante Valentine
Date: 4 June, 2021
"""

# CHALLENGE 1 (Print contents of a document already on computer)
import os
dojotext = os.path.join("C:\\","Users", "Toi", "Desktop", "Python", "dojo.txt")
dojotext2 = os.path.join("C:\\","Users", "Toi", "Desktop", "Python", "dojo2.txt")

dojo = open(dojotext,"r")
print(dojo.read())
dojo.close()

with open(dojotext2, "r") as f:
    print(f.read())

# CHALLENGE 2 (write a program that asks user a question and saves answer to a file)
datadoc = "datadoc.txt"
fname = input("What is your first name?\n > ")

with open(datadoc, "w") as f:
    f.write(fname)

# CHALLENGE 3 (Take items in the given list of lists and write to a csv with data from each list in its own row)
import csv
listcsv = "listcsv.csv"

givenlist = [["Top Gun", "Risky Business", "Minority Report"],["Titanic", "The Revenant", "Inception"],["Training Day", "Man on Fire", "Flight"]]
with open("listcsv", "w") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(givenlist[0])
    w.writerow(givenlist[1])
    w.writerow(givenlist[2])

