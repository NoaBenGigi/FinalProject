# ~~~~~~~~~~~~~~ FINAL PROJECT ~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~ NOA BEN-GIGI   318355633 ~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~ LION DAHAN     318873338 ~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~ YAM HARUSH     318886058  ~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~ MICHAEL HARUSH 208829085 ~~~~~~~~~~~~~~

# generate random integer values

from random import randint

# seed random number generator

listOfID = {"318355633", "318873338", "318886058", "208829085"}


def randomNumFromID(id, startRange, endRange):
    value = 0
    randIndexID = randint(1, 9)
    if startRange >= 10:
        value = randint(int(startRange / 10), int(endRange / 10))
        value = str(value) + id[randIndexID - 1]
    else:
        value = str(id[randIndexID - 1])
        value = int(value)
    return int(value)


def main():
    print("From questions 1-9 we need one question")  # rand the first question
    print(randomNumFromID("318355633", 1, 9))

    print("From questions 10-18 we need 2 questions")  # rand the 2nd,3rd question
    num1 = randomNumFromID("318355633", 10, 18)
    while not 10 <= num1 <= 18:
        num1 = randomNumFromID("318355633", 10, 18)
    print(num1)
    num2 = randomNumFromID("318873338", 10, 18)
    while not 10 <= num2 <= 18 or num2 == num1:
        num2 = randomNumFromID("318873338", 10, 18)
    print(num2)

    print("From questions 19-30 we need 2 questions")  # rand the 4th,5th question
    num1 = randomNumFromID("318873338", 19, 30)
    while not 19 <= num1 <= 30:
        num1 = randomNumFromID("318873338", 19, 30)
    print(num1)
    num2 = randomNumFromID("318886058", 19, 30)
    while not 19 <= num2 <= 30 or num2 == num1:
        num2 = randomNumFromID("318886058", 19, 30)
    print(num2)

    print("From questions 31-36 we need one question") # rand the 6th question
    num1 = randomNumFromID("208829085", 31, 36)
    while not 31 <= num1 <= 36:
        num1 = randomNumFromID("208829085", 31, 36)
    print(num1)


if __name__ == "__main__":
    main()
