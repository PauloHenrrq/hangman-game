# Arquivo principal onde estará o conteúdo final.

from randomize import randomize
from letters import letters
from verify import verify, process_atempt

def hangman_game():
    palavra = randomize()
    letras_corretas = []
    letras_incorretas = []
    numero_tentativas = 6

    print("Bem-vindo ao Jogo da Forca! 🚪")

    while numero_tentativas > 0:
        print("/nPalavra: ", letters(palavra, letras_corretas))
        print(f"Letras corretas: {', '.join(letras_corretas) if letras_corretas else "Nenhuma"}")
        print(f"Letras incorretas: {', '.join(letras_incorretas) if letras_incorretas else "Nenhuma"}")
        print(f"Tentativas Restantes: {numero_tentativas}")

        tentativa = input(str("Escreva uma letra: ")).lower()

        if (len(tentativa) > 1 or tentativa == ''):
            print("Você pode escrever somente 1 letra!")
            break   
