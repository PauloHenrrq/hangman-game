from src.database_fake import choice_word, secret_choice_word, incorrect_letters, max_attempt, moves
from src.verify import verify_attempt, check_full_word


def hangman_game(choice_word, secret_choice_word, incorrect_letters, max_attempt, moves):
    # print(choice_word)
    print("Bem-vindo ao Jogo da Forca! 🚪")
    while max_attempt > 0:
        print(f"Palavra: {"".join(secret_choice_word)} ")
        print(f'Você tem {max_attempt} tentativas \n')
        

        if max_attempt == 1:
            print('Essa é sua última tentativa. CUIDADO!')

        choice_user = input(str("Escreva uma letra: ")).lower()

        if (len(choice_user) > 1):
            choice_user = choice_user[0]

        if choice_user:
            index_letters = verify_attempt(choice_user, choice_word, incorrect_letters)

        if index_letters:
            for index in index_letters:
                secret_choice_word[index] = choice_user
        else:
            max_attempt -= 1


        if max_attempt == 0:
            print('Game Over macho véi')

        check_word = check_full_word(secret_choice_word)
        
        moves +=1
        if check_word:
            print(f'\nParabéns, você alcançou seu resultado em {moves} jogadas ')
            print(f'A palavra era: {choice_word}')
            print(f'Letras que você errou: {incorrect_letters}')
            break


hangman_game(choice_word, secret_choice_word, incorrect_letters, max_attempt, moves)
