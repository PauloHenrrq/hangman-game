# Criar uma função para escolher aleatóriamente uma palavra do dicionário;

import random

def randomize(categories):
    print("Bem-vindo ao Jogo da Forca! 🚪\n")
    print('Escolha uma categoria abaixo\n')
    for id, category in enumerate(categories):
        print(f'-> {category}')

    category_choice = False
    while not category_choice:
        choice_user = input('\nEscolha sua categoria: ').lower()
        
        if choice_user in categories:
            category_choice = choice_user
            

    random_word = random.choice(categories[category_choice])
    

    return random_word


