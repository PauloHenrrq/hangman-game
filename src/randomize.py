# Criar uma função para escolher aleatóriamente uma palavra do dicionário;

import random

def randomize():

    palavras = ["maçã", "banana", "laranja", "morango", "kiwi","sol","lua","programação","casa"," escola"," bairro" "escritor", "acampamento","lógica","borboleta","livro","celular","computador","praça","tela","cabelo","país","sábado","semana","tablet","bolo", "escrito","literatura","caderno","música","site","vampiro","frutas","açai","sal","shopping","igreja","etapas","vida","ciclo", "massa","regra","deletar","amor","aleatoriamente","alfa","cachorro","gato","carro","moto","cidade","professores","curso", "celular","aplicativos","palavras","pessoas","inteligentes","beleza","natureza","escolaridae","profissionais","jogos","natal", "comunidade","escolhida","sentimento","parque","árvore","criança","belo","dia","felicidades","amigos","artificial","valores", "casamento","cantoria","seleção","causa","matemática","física","aplicativo","moradia","papelaria","python","java","espaço","livre", "liberdade","fama","riqueza","amigos","colegas","escritores","livraria","conjuntos","navegação","filmes","pesquisar","luz","nascimento", "morada","estudos","redação","mouse","fotos","aprovado","data","nublado","trabalho","noivado","namoro","passeio","férias","aula"]

    palavra_aleatoria = random.choice(palavras)
    
    return palavra_aleatoria
