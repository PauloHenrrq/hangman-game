from .randomize import randomize

choice_word = randomize()

secret_choice_word = ['_' for letter in choice_word]

max_attempt = 6

incorrect_letters = []