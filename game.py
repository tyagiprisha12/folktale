import random
lifeline1available = True
lifeline2available = True
lifeline3available = True
gamerunning = True
print("Welcome to Who Will Become A Millionaire, the world's first Python trivia game show!")
print("")
name = input(("I am Bamitabh Achchan, your host for today! And you are? ")).strip().capitalize()
print("Alright, " + name + ", the rules are simple. Type A, B, C or D for your answer choice. If you are stuck, use a lifeline!")
print("Type 1 for 50:50, which erases two wrong options. Type 2 for a hint. Type 3 to change the question.")
input("Shall we begin? ")
print("")

q1 = [
    {
        "question": """Which is the only letter that does not appear in a U.S state name?
    A) Z   B) W   C) X   D) Q""",
        "answer": "D",
        "hint": " It is almost always followed by the letter 'U'.",
        "5050": "C) X   D) Q"
    },
    {
        "question": """Which is the only sea on earth with no coastline?
    A) Sargasso Sea   B) North Sea
    C) Bering Sea      D) Baltic Sea""",
        "answer": "A",
        "hint": " It is located in the North Atlantic Ocean, and is named after a type of floating seaweed.",
        "5050": "A) Sargasso Sea   D) Baltic Sea"
    },
    {
        "question": """Which singer holds the record for most Grammys won by any individual?
    A) Taylor Swift   B) Beyonce
    C) Stevie Wonder  D) Alison Krauss""",
        "answer": "B",
        "hint": " They rose to fame in the 1990s as the lead singer of an R&B group.",
        "5050": "A) Taylor Swift   B) Beyonce"
    },
    {
       "question": """What was Disney's first feature-length animated film?
    A) Snow White and the Seven Dwarfs B) Pinocchio
    C) Fantasia                        D) Dumbo""",
       "answer": "A",
       "hint": " It was released in 1937, and involves a poisonous apple and a magic mirror.",
       "5050": "A) Snow White and the Seven Dwarfs   C) Fantasia"
    },
    {
        "question": """What element makes up the majority of the Sun's mass?
        A) Carbon   B) Oxygen
        C) Hydrogen D) Helium""",
        "answer": "C",
        "hint": " It is the lightest element in the periodic table.",
        "5050": "C) Hydrogen   D) Helium"
    },
    {
        "question": """Which jagged peaks form the natural border between France and Spain?
        A) The Alps      B) The Dolomites
        C) The Apennines D) The Pyrenees""",
        "answer": "D",
        "hint": " The country of Andorra is completely landlocked within this mountain range.",
        "5050": "A) The Alps   D) The Pyrenees"
    }
    
]


random.shuffle(q1)
randomq1 = q1.pop()
print(randomq1["question"])
while True:
    ans = input("Answer: ").upper().strip()
    if ans == randomq1["answer"]:
        print("Congratulations! You answered correctly and won $100.")
        break
    elif ans == "1":
        if lifeline1available:
            lifeline1available = False
            print("50:50 activated! Your remaining options are: " + randomq1["5050"])
        else:
            print("You have already used this lifeline.")
    elif ans == "2":
        if lifeline2available:
            lifeline2available = False
            print("Hint activated! Your hint is:" + randomq1["hint"])
        else:
            print("You have already used this lifeline.")
    elif ans == "3":
        if lifeline3available:
            lifeline3available = False
            randomq1 = q1.pop()
            print("Question Swap activated! Your new question is:")
            print(randomq1["question"])
        else:
            print("You have already used this lifeline.")
    else:
            print("Unfortunately, that's wrong... Game over!")
            gamerunning = False
            break

if gamerunning:
    random.shuffle(q1)
    randomq1 = q1.pop()
    print(randomq1["question"])
    while True:
        ans = input("Answer: ").upper().strip()
        if ans == randomq1["answer"]:
            print("Congratulations! You answered correctly and won $200.")
            break
        elif ans == "1":
            if lifeline1available:
                lifeline1available = False
                print("50:50 activated! Your remaining options are: " + randomq1["5050"])
            else:
                print("You have already used this lifeline.")
        elif ans == "2":
            if lifeline2available:
                lifeline2available = False
                print("Hint activated! Your hint is:" + randomq1["hint"])
            else:
                print("You have already used this lifeline.")
        elif ans == "3":
            if lifeline3available:
                lifeline3available = False
                randomq1 = q1.pop()
                print("Question Swap activated! Your new question is:")
                print(randomq1["question"])
            else:
                print("You have already used this lifeline.")
        else:
                print("Unfortunately, that's wrong... Game over!")
                gamerunning = False
                break

if gamerunning:
    random.shuffle(q1)
    randomq1 = q1.pop()
    print(randomq1["question"])
    while True:
        ans = input("Answer: ").upper().strip()
        if ans == randomq1["answer"]:
            print("Congratulations! You answered correctly and won $300.")
            break
        elif ans == "1":
            if lifeline1available:
                lifeline1available = False
                print("50:50 activated! Your remaining options are: " + randomq1["5050"])
            else:
                print("You have already used this lifeline.")
        elif ans == "2":
            if lifeline2available:
                lifeline2available = False
                print("Hint activated! Your hint is:" + randomq1["hint"])
            else:
                print("You have already used this lifeline.")
        elif ans == "3":
            if lifeline3available:
                lifeline3available = False
                randomq1 = q1.pop()
                print("Question Swap activated! Your new question is:")
                print(randomq1["question"])
            else:
                print("You have already used this lifeline.")
        else:
                print("Unfortunately, that's wrong... Game over!")
                gamerunning = False
                break

if gamerunning:
    random.shuffle(q1)
    randomq1 = q1.pop()
    print(randomq1["question"])
    while True:
        ans = input("Answer: ").upper().strip()
        if ans == randomq1["answer"]:
            print("Congratulations! You answered correctly and won $400.")
            break
        elif ans == "1":
            if lifeline1available:
                lifeline1available = False
                print("50:50 activated! Your remaining options are: " + randomq1["5050"])
            else:
                print("You have already used this lifeline.")
        elif ans == "2":
            if lifeline2available:
                lifeline2available = False
                print("Hint activated! Your hint is:" + randomq1["hint"])
            else:
                print("You have already used this lifeline.")
        elif ans == "3":
            if lifeline3available:
                lifeline3available = False
                randomq1 = q1.pop()
                print("Question Swap activated! Your new question is:")
                print(randomq1["question"])
            else:
                print("You have already used this lifeline.")
        else:
                print("Unfortunately, that's wrong... Game over!")
                gamerunning = False
                break

if gamerunning:
    random.shuffle(q1)
    randomq1 = q1.pop()
    print(randomq1["question"])
    while True:
        ans = input("Answer: ").upper().strip()
        if ans == randomq1["answer"]:
            print("You answered correctly and won $1,000,000!")
            break
        elif ans == "1":
            if lifeline1available:
                lifeline1available = False
                print("50:50 activated! Your remaining options are: " + randomq1["5050"])
            else:
                print("You have already used this lifeline.")
        elif ans == "2":
            if lifeline2available:
                lifeline2available = False
                print("Hint activated! Your hint is:" + randomq1["hint"])
            else:
                print("You have already used this lifeline.")
        elif ans == "3":
            if lifeline3available:
                lifeline3available = False
                randomq1 = q1.pop()
                print("Question Swap activated! Your new question is:")
                print(randomq1["question"])
            else:
                print("You have already used this lifeline.")
        else:
                print("Unfortunately, that's wrong... Game over!")
                gamerunning = False
                break

if gamerunning:
    print("Congratulations, You have become a millionaire!")