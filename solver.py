"""Основной модуль с решателем"""
def solve(a: float = 0, b: float = 0, c: float = 0) -> str:
    """Решатель принимает три коэффицента и возвращает строку с ответом"""
    if a == 0:
        if b == 0:
            if c == 0:
                return "X - любое число"
            else:
                return "X - не существует"
        else:
            return "X = {}".format(- c / b)
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            return "X - не существует"
        elif d == 0:
            return "X = {}".format(-b / (2 * a))
        else:
            return "Два решения: X1 = {}, X2 = {}".format(((-b + d ** 0.5) / (2 * a)), ((-b - d ** 0.5) / (2 * a)))
