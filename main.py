import random


a = ["dog", "mouse", "cat"]
word = random.choice(a)
print(len(word))
count = 0
#Lives in the game
lives = 6
#location of the character in the word
location = 0

used = ""


def new_guess(guess):
    global count
    global lives
    global location
    global used

    if guess not in used:
        used += guess
        if guess in word:
            for n in word:
                if n == guess:
                    count += 1
        else:
            print("Try Again")
            lives -= 1
    else:
        print("You tried this letter already")


# Keep playing
while len(word) > count and lives > 0:
    answer = ""
    for letter in word:
        if letter in used:
            answer += letter
        else:
            answer += "_"
    print(answer)
    letter = input("Enter a letter: ")
    new_guess(letter)
if lives == 0:
    print("Loser")
else:
    print("You are a winner!")