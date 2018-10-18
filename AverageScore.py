total = 0
count = 0
maxScore = 100
action = "continue"


while action != "stop":

    print("Please input a score:", end = " ")
    score = int(input())

    if score < 1:
        if score == 0:
            action = "analyse"
        else:
            action = "stop"

    else:
        if score > maxScore:
            action = "error"

    if action == "continue":
        count = count + 1
        total = total + score

    elif action == "error":
        print("Score exceeds ", maxScore)
        action = "continue"

    elif action == "analyse":
        if count > 0:
            average = total / count
            print("Average: ", average)
        else:
            print("No values have been input")
        action = "continue"

    elif action == "stop":
        if count > 0:
            average = total / count
            print("Average: ", average)
        else:
            print("No values have been input")


           


