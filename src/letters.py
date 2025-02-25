# Fazer a troca da letra correta pela posição respectiva na palavra selecionada;

def letters(palavra, letra_verificada):
    print(palavra)
    indice = (palavra.find(letra_verificada))
    palavra_secreta = list("_" * len(palavra))
    palavra_secreta[indice] = letra_verificada
    print(palavra,palavra_secreta)
