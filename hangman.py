# encodeing utf-8
def hangman(word):
    wrong = 0
    stages = ["",
              "_________           ",
              "|        |          ",
              "|        O          ",
              "|       /|\         ",
              "|       / \         ",
              "|                   "
    ]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("Welcome to Hangman!")

while(wrong < len(stages) - 1):
    print("\n")
    msg = "Expect  a word."
    char = input(msg)
    if char in rletters.index(char):
        board[cind] = char
        rletters[cind] = '$'
    else:
        wrong += 1
