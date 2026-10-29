print(" Welcome to my computer quiz! ")

playing =input("Do you want to play ?")
print(playing)

if playing.lower() !="yes":
    quit()

print("Okay! lets play :)")
score=0

answer = input("What does CPU stand for ?")
if answer.lower()=="central processing unit":
    print("Correct !!")
    score+=1
else:
    print("Incorrect !!")

answer = input("What does GPU stand for ?")
if answer.lower()=="graphics processing unit":
    print("Correct !!")
    score+=1
else:
    print("Incorrect !!")

answer = input("What does RAM stand for ?")
if answer.lower()=="random access memory":
    print("Correct !!")
    score+=1
else:
    print("Incorrect !!")

answer = input("What does ROM stand for ?")
if answer.lower()=="read-only memory":
    print("Correct !!")
    score+=1
else:
    print("Incorrect !!")

print(f"You got {score}/4 questions correct !")

print(f"You got {(score/4)*100} % ")
