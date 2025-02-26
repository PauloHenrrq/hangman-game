from .randomize import randomize

choice_word = randomize()

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
