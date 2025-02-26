from .randomize import randomize

choice_word = randomize()
# 'flauta'

secret_choice_word = ['_' for letter in choice_word]
# ["_", "_", "_", "_","_", "_"]


max_attempt = 6
# máximo de tentativas

moves = 0
# Cada jogada do usuário

incorrect_letters = []
# Lista que conterá todas as letras que o usuário errar

