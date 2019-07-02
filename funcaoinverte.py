def reverse_odd(txt):
    """
    Função que inverte palavras da frase que tiverem tamanho ímpar.

    """

    box = []
    res = txt.split(' ')
    for x in res:
        if (len(x) % 2) == 1:
            box.append(x[:: -1])
        else:
            box.append(x)
    print(' '.join(box))
