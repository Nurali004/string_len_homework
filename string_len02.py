def main(a):
    """
    A string type variable is given. Return True if its length is even. Return False if its length is odd.

    Args:
        a (str): string

    Returns:
        bool: True or False
    """
    if len(a) % 2 == 0:
        return True
    else:
        return False

# Sinov
a = "fjfhfhdhgshgs"
print(main(a))  # False, chunki uzunligi 13 (toq)

