import sys


def verifica_pari(n):
    """
    Verifica se n e' pari
    """
    if (n % 2 == 0):
        return True
    else:
        return False


def verifica_potenza_2(n):
    """
    Verifica se n e' potenza di 2
    """
    if (n != 0 and ((n & (n - 1)) == 0)):
        return True
    else:
        return False


def verifica_primo(n): # pragma: no cover
    """
    verifica se n e' primo
    """
    pass

def main(argv):
    # Verifico presenza argomento
    try:
        arg = argv[1]
    except:
        print("Nessun argomento passato")
        return


    # Verifico argomento intero
    try:
        num = int(arg)
    except:
        print("Argomento non intero")
        return

    if verifica_pari(num):
        print("pari")
        if verifica_potenza_2(num):
            print("potenza di 2")
    else:
        print("dispari")
        if num == 1:
            print("uguale ad 1")
        else:
            print("diverso da 1")
