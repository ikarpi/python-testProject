def remainder(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо")
    return dividend % divisor