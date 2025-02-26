def verify_attempt(choice_user, choice_word, incorrect_letters):

    if choice_user in choice_word:
        indexes = [i for i, letter in enumerate(choice_word) if letter == choice_user]
        return indexes
    incorrect_letters.append(choice_user)
    return None


def check_full_word(secret_choice_word):
    for letter in secret_choice_word:
        if letter == '_':
            return False
    return True