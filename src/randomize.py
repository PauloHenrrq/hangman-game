# Criar uma função para escolher aleatóriamente uma palavra do dicionário;

import random

def randomize():

    palavras = ["cebola", "banana", "laranja", "morango", "kiwi","sol","lua","ouvido","casa"," escola"," bairro","escritor",
    "acampamento","nome","borboleta","livro","celular","computador","linguagem","tela","cabelo","estado","domingo","semana","tablet","bolo",
    "escrito","literatura","caderno","mais","site","vampiro","frutas","caju","sal","shopping","igreja","etapas","vida","ciclo",
    "massa","regra","deletar","amor","aleatoriamente","alfa","cachorro","gato","carro","moto","cidade","professores","curso",
    "celular","aplicativos","palavras","pessoas","inteligentes","beleza","natureza","escolaridae","profissionais","jogos","natal",
    "comunidade","escolhida","sentimento","parque","planta","criança","belo","dia","felicidades","amigos","artificial","valores",
    "casamento","cantoria","print","causa","filosofia","geografia","aplicativo","moradia","papelaria","python","java","espaço","livre",
    "liberdade","fama","riqueza","amigos","colegas","escritores","livraria","conjuntos","navio","filmes","pesquisar","luz","nascimento",
    "morada","estudos","aberto","mouse","fotos","aprovado","data","nublado","trabalho","noivado","namoro","passeio","galinha","aula"]

    palavra_aleatoria = random.choice(palavras)
    
    return palavra_aleatoria
