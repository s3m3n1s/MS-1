"""Основной модуль с решателем"""


def solve(a: float = 0, b: float = 0, c: float = 0) -> str:
    """Решатель принимает три коэффицента и возвращает строку с ответом"""
    xs = calculate(a, b, c)
    if type(xs) is bool:
        return "X - любое число"
    if not xs:
        return "X - не существует"
    if len(xs) == 1:
        return "X = {}".format(xs[0])
    if len(xs) == 2:
        return "Два решения: X1 = {}, X2 = {}".format(xs[0], xs[1])
    return str(xs)


def calculate(a: float = 0, b: float = 0, c: float = 0) -> list[float] | bool:
    """Калькулятор принимает три коэффицента и возвращает список ответов, если x - любое число, возвращает True"""
    if a == 0:
        if b == 0:
            if c == 0:
                return True
            else:
                return []
        else:
            return [- c / b]
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            return []
        elif d == 0:
            return [-b / (2 * a)]
        else:
            return [(-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)]
