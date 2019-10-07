from random import choices
from string import ascii_lowercase, ascii_uppercase, digits

alpha_nums = ascii_lowercase + ascii_uppercase + digits


def get_unique_id(n):
    """

    :param n: int Number of characters to use. Default to 8, default_id_length
    :return: str Random alphanumeric string of length n
    """
    letters = choices(alpha_nums, k=n)

    return "".join(letters)
