import random

def main():
    words_path = "./words.txt"
    words = get_words(words_path)
    computer_choice = random.choice(words)
    print(computer_choice)
    computer_word_length = len(computer_choice)
    print(f'Word is {computer_word_length} characters in length')
    score = 0
    while score != computer_word_length:
        player_choice = get_player_input()
        score, computer_choice = check_player_input(player_choice, computer_choice, score)
        print(score)
    print('You win!')

def check_player_input(player, computer, score):
    for i in computer:
        if player == i:
            computer = computer.replace(i, "")
            score += 1
            print(computer)
            return score, computer
        
    print("Incorrect!")
    computer = computer
    return score, computer     

def get_player_input():
    player_choice = input("enter input: ")
    while len(player_choice) > 1:
        player_choice = input("only enter 1 character: ")
    else:
        return player_choice

def get_words(path):
    with open(path) as f:
        words = [line.strip() for line in f]
    return words
    
main()