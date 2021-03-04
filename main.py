import sys

word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class State:
    def __init__(self, nr_st, prefix):
        self.nr_st: int = nr_st
        self.prefix = prefix


def make_delta(str1):
    # matricea rezultat
    delta = {}

    # lista de prefixe din pattern
    my_list = [str1[:i] for i in range(0, len(str1))]

    # lista de stari
    k = [State(i, str1[:i]) for i in range(0, len(str1))]

    # completez initial matricea cu empty
    for i in range(0, len(str1) - 1):
        for j in word:
            delta[(k[i].prefix, j)] = 0

    # cazul in care urmatoarea litera se potriveste cu prefixul pattern-ului
    for i in range(0, len(str1)):
        for j in word:
            if (k[i].prefix + j) in my_list:
                index = my_list.index(k[i].prefix + j)
            else:
                index = 0
            delta[(k[i].prefix, j)] = index

    # cazul in care urmatoarea litera nu se potriveste cu prefixul pattern-ului
    for i in range(0, len(str1)):
        for j in word:
            if (k[i].prefix + j) not in my_list:
                new_str = k[i].prefix + j
                p = [new_str[len(new_str) - 1 - i:] for i in range(0, len(new_str) - 1)]
                for c in p:
                    if c in my_list:
                        index = my_list.index(c)
                        delta[(k[i].prefix, j)] = index
    return delta


def parser(str1, str2, file):
    # rezultatul intors de functie
    result = ""

    # lista de prefixe din pattern
    my_list = [str1[:i] for i in range(0, len(str1))]

    # algoritmul Boyer-Moore
    q = 0

    # deschid fisierul pentru scriere
    f_out = open(file, "w")

    # matricea de prefixe
    delta = make_delta(str1)

    # parcurg textul in care caut pattern
    for i in range(0, len(str2) - 1):
        q = delta[(my_list[q], str2[i])]
        if q == len(str1) - 1:
            result += str(i - len(str1) - 1 + 3) + ' '
    result += '\n'

    # scriu in fisier
    f_out.write(result)

    # inchid fisierul in care am scris
    f_out.close()


def main():
    # deschid fisierul din care citire
    f_in = open(sys.argv[1], "r")

    # citesc datele de intrare
    pattern = f_in.readline()
    string = f_in.readline()

    # apelez functia care implementeaza metoda Boyer-Moore.
    parser(pattern, string, sys.argv[2])

    # inchid fisierul din care citesc
    f_in.close()


if __name__ == "__main__":
    main()
