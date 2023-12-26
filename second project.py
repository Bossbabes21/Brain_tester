print("Welcome to Brain Squeezer PREPARE TO BE CHALLENGED!!!")

min_score = 9
score = 0

play = input("Are you ready to play? Yes or No? ")

if play.lower() == "yes":
    print("Your first question is : ")
else:
    quit()


question = input("Who is the 23rd President? ")
if question.lower() != "benjamin harrison":
    print("Incorrect! The correct answer is Benjamin Harrison")
else:
    print("Correct!")
    score += 3
    print(score)

question = input("How many days does it take for the Earth to orbit the Sun? ")
if question.lower() != "365":
    print("Incorrect! The correct answer is 365")
else:
    print("Correct!")
    score += 3


question = input("What’s the national flower of Japan? ")
if question.lower() != "cherry blossom":
    print("Incorrect! The correct answer is cherry blossom")
else:
    print("Correct!")
    score += 3


question = input("What company was originally called Cadabra? ")
if question.lower() != "amazon":
    print("Incorrect! The correct answer is amazon")
else:
    print("Correct!")
    score += 3


print("Your current score is ", score)

if score < min_score:
    print("Sorry you failed Level 1.")
    play = input("Do you want to play level 1 again? ")
    if play.lower() == "yes":
        print("Your first question is : ")
    else:
        quit()

    question = input("What’s the smallest country in the world? ")
    if question.lower() != "vatican":
        print("Incorrect! The correct answer is vatican")
    else:
        print("Correct!")
        score += 3

    question = input("Name the longest river in the world? ")
    if question.lower() != "nile":
        print("Incorrect! The correct answer is nile")
    else:
        print("Correct!")
        score += 3

    question = input("What is the slang name for New York City, used by locals? ")
    if question.lower() != "gotham":
        print("Incorrect!The correct answer is gotham")
    else:
        print("Correct!")
        score += 3

    question = input("Name the best-selling book series of the 21st century?  ")
    if question.lower() != "harry potter":
        print("Incorrect! The correct answer is harry potter")
    else:
        print("Correct!")
        score += 3

    print("Your current score is ", score)
    if score < min_score:
             print("Sorry you failed Level 1 again!!")
             print("GAME OVER!!")

    else:
             print("You made it to level 2!!!")
             print("PREPARE TO BE CHALLENGED!!!")
             print("LEVEL 2 BEGINS NOW!!!")


else:
    print("You made it to level 2!!!")
    print("PREPARE TO BE CHALLENGED!!!")
    print("LEVEL 2 BEGINS NOW!!!")


#level up the code make it more intresting
    question = input("What word is spelled incorrectly in every single dictionary?  ")
    if question.lower() != "incorrectly":
        print("Incorrect! The correct answer is incorrectly.")
    else:
        print("Correct!")
        score += 3

    question = input("What is it that lives if it is fed, and dies if you give it a drink?  ")
    if question.lower() != "fire":
        print("Incorrect! The correct answer is fire.")
    else:
        print("Correct!")
        score += 3

    question = input("What goes up but never ever comes down? ")
    if question.lower() != "your age":
        print("Incorrect! The correct answer is your age.")
    else:
        print("Correct!")
        score += 3

    question = input("What do you call a women who knows where her husband is all the time? ")
    if question.lower() != "a widow":
        print("Incorrect! The correct answer is a widow.")
    else:
        print("Correct!")
        score += 3

    question = input("What goes up and down, but always remain in the same place? ")
    if question.lower() != "stairs":
        print("Incorrect! The correct answer is your stairs.")
    else:
        print("Correct!")
        score += 3

    print("LEVEL 2 COMPLETED!!")
    play = input("DO YOU STILL WANT TO CHALLANGE YOUR MIND?")
    if play.lower() == "yes":
        print("Your first question is : ")
    else:
        quit()