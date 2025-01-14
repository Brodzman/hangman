import random

def main():
    words_path = "./words.txt"
    words = get_words(words_path)
    computer_choice = random.choice(words)
    print(computer_choice)
    computer_word_length = len(computer_choice)
    print(f'The word to guess is {computer_word_length} characters in length')
    score = 0
    lives = 5
    while score != computer_word_length:
        player_choice = get_player_input()
        score, computer_choice, lives = check_player_input(player_choice, computer_choice, score, lives)
        print(f'You have guessed {score}/{computer_word_length}')
        if lives == 0:
            print('You lose!')
            return
    print('You win!')

def check_player_input(player, computer, score, lives):
    for i in range(0, len(computer)):
        print(computer[i])
        if player == computer[i]:
            computer = computer.replace(computer[i], "")
            score += 1
            print(computer)
            print('Correct!')
            return score, computer, lives
        
    print("Incorrect!")
    computer = computer
    lives -= 1
    print(f'You have {lives} attempts remaining')
    return score, computer, lives   

def get_player_input():
    player_choice = input("Enter your guess: ")
    while len(player_choice) > 1:
        player_choice = input("You may only enter 1 letter, try again: ")
    else:
        return player_choice

def get_words(path):
    with open(path) as f:
        words = [line.strip() for line in f]
    return words

main()
