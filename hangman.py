#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    file = open (file_name,'r')
    list = file.readlines()
    return list


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    ranchoice = random.randint(0, len(words) -1)
    words[0] = words[ranchoice]
    ranchoicelet = random.randint (0, len(words[0]) -1)
    print ("Guess the word: " + words[0][:ranchoicelet] + '_' + words [0][ranchoicelet + 1:])

    return words[0]

def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    answer = input("Guess the missing letter: ")
    return answer


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

