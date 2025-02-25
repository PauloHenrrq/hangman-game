# Arquivo principal onde estará o conteúdo final.

from src.randomize import randomize
from src.verify import process_atempt, verify_atempt
from src.letters import letters
# from letters import letters
# from verify import verify, process_atempt

def hangman_game():
    palavra = randomize()

    letras_corretas = []
    letras_incorretas = []
    numero_tentativas = 6

    print("Bem-vindo ao Jogo da Forca! 🚪")
    print(palavra)
    while numero_tentativas > 0:
        # print("/nPalavra: ", letters(palavra, letras_corretas))
        # print(f"Letras corretas: {', '.join(letras_corretas) if letras_corretas else "Nenhuma"}")
        # print(f"Letras incorretas: {', '.join(letras_incorretas) if letras_incorretas else "Nenhuma"}")
        # print(f"Tentativas Restantes: {numero_tentativas}")

        letra_digitada = input(str("Escreva uma letra: ")).lower()

        if (len(letra_digitada) > 1 or letra_digitada == ''):
            print("Você pode escrever somente 1 letra!")
            break

        letra_verificada = process_atempt(palavra, letra_digitada)

        if letra_verificada:
            letras_corretas.append(letra_verificada)
        else:
            numero_tentativas -=1
            letras_incorretas.append(letra_digitada)

    resultaodo = verify_atempt(palavra, letras_corretas)


hangman_game()

