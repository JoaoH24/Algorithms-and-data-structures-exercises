number = int(input("Ingrese un número: "))
h = 0


def math_funt(n, h):
    if n == 0:
        return 1
    if n >= 1:
        h += 1 / n
        return h + math_funt(n - 1, h)


print(math_funt(number, h))
