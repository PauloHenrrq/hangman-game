def process_atempt(palavra, letra_digitada):

    if letra_digitada in palavra:
        return letra_digitada
    
    return None


def verify_atempt(palavra, letras_corretas):
    tamanho_temp = 0
    for letra in letras_corretas:
        if letra in palavra:
            tamanho_temp += palavra.count(letra)
            if len(palavra) == tamanho_temp:
                return('Você acertou')
                
    


    