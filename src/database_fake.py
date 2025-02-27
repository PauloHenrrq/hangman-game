from .randomize import randomize
categories = {
    "animais": ["cachorro", "gato", "elefante", "leao", "tigre", "girafa", "jacare", "pato", "cobra", "macaco"],
    "frutas": ["banana", "maca", "laranja", "uva", "abacaxi", "melancia", "mamao", "morango", "kiwi", "cereja"],
    "cores": ["vermelho", "azul", "amarelo", "verde", "roxo", "laranja", "preto", "branco", "cinza", "rosa"],
    "paises": ["brasil", "argentina", "portugal", "canada", "japao", "alemanha", "italia", "franca", "espanha", "mexico"],
    "objetos": ["cadeira", "mesa", "computador", "telefone", "janela", "caderno", "lapis", "mochila", "teclado", "relógio"]
}

choice_word = randomize(categories)


secret_choice_word = ['_' for letter in choice_word]

hangman_stages = [
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |   
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |   
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   
       |   
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |   
       |   
    """,
    """
       ------
       |    |
       |    O
       |    |
       |   
       |   
    """,
    """
       ------
       |    |
       |    O
       |   
       |   
       |   
    """,
    """
       ------
       |    |
       |    
       |   
       |   
       |   
    """,
]

max_attempt = 7


moves = 0


incorrect_letters = []
