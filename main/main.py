print("Welcome to my Quiz")

playing=input("Do you want to Play ? ")
if playing.lower() != "yes":
    quit()

print ("Okay! Let's Play:) ")

answer = input ("(1) What Does CPU stands for ? ")
if answer.lower() == "central processing unit" :
    print("Correct!")
else:
    print("Incorrect!")

answer = input ("(2) What Does GPU stands for ? ")
if answer.lower() == "graphic processing unit" :
    print("Correct!")
else:
    print("Incorrect!")

answer = input ("(3) What Does RAM stands for ? ")
if answer.lower() == "random access memory" :
    print("Correct!")
else:
    print("Incorrect!")

answer = input ("Which semiconductor is mainly used in electroninc devices ? ")
if answer.lower() == "silicon" :
    print("Correct!")
else:
    print("Incorrect!")

