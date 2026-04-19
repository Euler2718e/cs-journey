import time
import random

print(" ")
topic = input(
    "Choose a topic between coding (en), calculus (en), physics (n) and pop-science (n). Answer co/ca/ph/po: ")

if topic == "co":
    from questions import coding_en
    questions = coding_en

elif topic == "ca":
    from questions import calculus_en
    questions = calculus_en

elif topic == "ph":
    from questions import fysikk_no
    questions = fysikk_no

elif topic == "po":
    from questions import popvitenskap_no
    questions = popvitenskap_no


random.shuffle(questions)
start = time.time()

with open("highscore.txt", "r") as f:
    # high_score = int(f.read())
    try:
        high_score = int(f.read())
    except ValueError:
        high_score = 0  # no score yet


def clear_ansi():
    print("\033[H\033[J", end="")


score = 0
num = -1
amount = len(questions)
num = -1

for question in questions:

    clear_ansi()

    order = []
    num += 1
    dir = questions[num]
    r_ans = dir["answer"]
    order.append(r_ans)
    w_ans1 = dir["wrong"][0]
    order.append(w_ans1)
    w_ans2 = dir["wrong"][1]
    order.append(w_ans2)

    random.shuffle(order)

    A = order[0]
    B = order[1]
    C = order[2]

    if A == r_ans:
        correct = "A"
    elif B == r_ans:
        correct = "B"
    elif C == r_ans:
        correct = "C"

    q = questions[num]

    print(" ")
    print(q["question"])
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C: {C}")

    answer = str(correct)

    print(" ")
    p_answer = str(input("Write you answer here: "))

    if p_answer.upper() == answer:
        clear_ansi()
        print(" ")
        print("Correct! Good job")
        score += 1
        print(" ")
        print(f"Current score: {score}")

    else:
        print(" ")
        print(f"Wrong, the answer was '{correct}: {r_ans}' ")
        print(f"Current score: {score}")

    print(" ")
    cont = input("Continue? Press ""enter"" for yes, ""space + enter"" for no")

    if cont == " ":
        break

if score > high_score:
    clear_ansi()
    high_score = score
    print(f"New high score: {score}!")

    with open("highscore.txt", "w") as f:
        f.write(str(high_score))

end = time.time()
elapsed = end - start

print(" ")
print(f"Good job! You managed to answer {score} questions out of {amount}")
print(f"It took {elapsed:.1f} seconds")
