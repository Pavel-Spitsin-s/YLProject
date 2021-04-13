import random as rd


def MakeTok():
    tok = []
    strtok = ''
    for i in range(2):
        tok.append(rd.choice(['A','B','C','D','E','F','G','H']))

    for i in range(4):
        tok.append(str(rd.randint(0, 9)))
    rd.shuffle(tok)
    for i in tok:
        strtok += i
    return strtok