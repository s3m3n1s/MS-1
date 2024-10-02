"""Основной модуль с решателем"""

from math import sqrt, cbrt

def solve_kvadro(a: float = 0, b: float = 0, c: float = 0) -> str:
    """Решатель принимает три коэффицента и возвращает строку с ответом"""
    xs = calculate(a, b, c)
    if type(xs) is bool:
        return "X - любое число"
    if not xs:
        return "X - не существует"
    if len(xs) == 1:
        return "X1 = {}".format(xs[0])
    if len(xs) == 2:
        return "Решения: X1 = {}, X2 = {}".format(xs[0], xs[1])
    return str(xs)


def solve(a: float = 0, b: float = 0, c: float = 0, d: float = 0) -> str:
    """Решатель принимает четыре коэффицента и возвращает строку с ответом"""
    if a == 0: return solve_kvadro(b, c, d)
    if d == 0: return "X = 0, решение оставшегося квадратного уравнения: \n" + solve_kvadro(a, b, c)
    import cmath
    p = (3*a*c - b**2)/(3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d)/(27*a**3)
    

    Q = (p/3)**(3) + (q/2)**(2)

    
    if Q == 0:
        x1 = 2 * (-q / 2) ** (1 / 3) - b / (3 * a)
        x2 = (-q / 2) ** (-1 / 3) - b / (3 * a)
        x3 = (-q / 2) ** (-1 / 3) - b / (3 * a)
        if p==q and p==0:
            return "Один трёхкратный вещественный корень X = {}".format(x1)
        return "Один однократный вещественный корень X1 = {} и один двукратный X2 = {}".format(x1, x2)

    if Q > 0:
        preAlpha = (-(q/2)+sqrt(Q))
        Alpha = cbrt(preAlpha)# * (preAlpha/abs(preAlpha))
        preBeta = (-(q/2)-sqrt(Q))
        Beta = cbrt(preBeta)# * (preBeta/abs(preBeta))
        y1 = Alpha + Beta
        y2 = complex(-((Alpha + Beta) / 2), (Alpha - Beta) / 2 * 3 ** 0.5)
        y3 = complex(-((Alpha + Beta) / 2), -(Alpha - Beta) / 2 * 3 ** 0.5)
        x1 = y1 - b / (3 * a)
        x2 = y2 - b / (3 * a)
        x3 = y3 - b / (3 * a)

        return "Один вещественный корень X1 = {} и два сопряжённых комплексных корня X2 = {}, X3 = {}".format(x1.real, x2, x3)
    
    if Q < 0:
        if q == 0:
            F = cmath.pi/2
        if q < 0:
            F = cmath.atan(-2 * cmath.sqrt(-Q) / q)
        if q > 0:
            F = cmath.atan(-2 * cmath.sqrt(-Q) / q) + cmath.pi
        x1 = 2 * (-p / 3)**0.5 * cmath.cos(F / 3) - b / (3 * a)
        x2 = 2 * (-p / 3)**0.5 * cmath.cos((F / 3) + 2 * cmath.pi / 3) - b / (3 * a)
        x3 = 2 * (-p / 3)**0.5 * cmath.cos((F / 3) + 4 * cmath.pi / 3) - b / (3 * a)
        
        return "Три вещественных корня  {}, {}, {}".format(x1.real, x2.real, x3.real)

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
