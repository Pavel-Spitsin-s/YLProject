R_PAD = [2, 3, 4]
M_FORM = [5, 6, 7, 8, 9, 0]


def check_correct(num):
    try:
        num = int(num)
        if num < 1:
            return 1
        elif num % 10 == 1:
            return str(num) + " место"
        elif num % 10 in R_PAD:
            return str(num) + " места"
        elif num % 10 in M_FORM and num != 0:
            return str(num) + " мест"
        else:
            return 1
    except Exception:
        return 1
