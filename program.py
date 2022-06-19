import time


def main(version: int):
    """this function prints the current version of the program.

    Args:
        version (int): the current version of the program.
    """
    while True:
        time.sleep(.5)
        print(version)
