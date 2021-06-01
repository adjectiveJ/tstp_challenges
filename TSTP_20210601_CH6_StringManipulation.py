"""
The Self-Taught Programmer - Chapter 6 Challenges
Author: Dante Valentine
Date: 1 June, 2021
"""

# CHALLENGE 1
for c in "camus":
   print(c)

# CHALLENGE 2
str1 = input("What did you write? ")
str2 = input("Who did you send it to? ")
str3 = "Yesterday I wrote a {}. I sent it to {}!".format(str1, str2)
print(str3)

# CHALLENGE 3
# print("aldous Huxley was born in 1894.".capitalize())

# CHALLENGE 4
str4 = "Where now? Who now? When now?"
questions = str4.split("? ")
for i in range(0,len(questions)-1):
    questions[i] += "?"
print(questions)

# CHALLENGE 5
list1 = ["The", "fox", "jumped", "over", "the", "fence", "."]
list1 = " ".join(list1[0:6]) + list1[6]
print(list1)

# CHALLENGE 6
print("A screaming comes across the sky".replace("s","$"))

# CHALLENGE 7
str5 = "Hemingway"
print(str5.index("m"))

# CHALLENGE 8
str6 = "\"That's not fair.\" I wrap my arms around myself. \"I'm fighting, too.\"\n\"Well, seeing as your father created this mess, if I were you, I'd fight a little harder.\""
print(str6)

# CHALLENGE 9
str7 = "three" + " " + "three" + " " + "three"
print(str7)
str8 = "three " * 3
str8 = str8[0:(len(str8)-1)]
print(str8)

# CHALLENGE 10
str8 = "It was a bright cold day in April, abd the clocks were striking thirteen."
sliceindex = str8.index(",")
str9 = str8[0:sliceindex]
print(str9)