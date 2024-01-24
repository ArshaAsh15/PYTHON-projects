# my first project using python
# QUIZ GAME

print("welcome to my game space")

playing = input("Do you want to play?  ")

if playing != "yes":
    quit()

age = int(input ("What's your age? "))
if age > 18:
    print("I'm a " + str(age) + " year,adult")
elif age > 12:
    print ("I'm a " + str(age) + " year,teen")
else:
    print ("I'm a " + str(age) + " year,kid")

answer = input ("Which level of game do you want to play easy,medium,hard: ")
if answer.lower() == "easy":
    print ("here comes the easy level")
elif answer.lower() == "medium":
    print ("here comes the medium level")
else:
    print ("here comes the hard level")

print("okay! Let's play ")
score = 0

answer = input ("What's your name?  ")
print(" nice meeting you. ")

answer = input("What does CPU stand for?  ")
if answer == "central processing unit":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for?  ")
if answer == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for?  ")
if answer == "random access memory":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("250/5?  ")
if answer == "50":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("75*2+20 ?  ")
if answer == "170":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("15+25-5+6*8?  ")
if answer == "83":
    print("correct")
    score += 1
else:
    print("Incorrect")

print ("You got " + str(score)  + " questions correct!")








