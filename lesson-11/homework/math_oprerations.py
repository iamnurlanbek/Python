
def add(a, b):
    return f"Addition: {a + b}"

def substract(a, b):
    return f"Substraction: {a - b}"

def multipy(a, b):
    return f"Multiplication: {a * b}"

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Sonni 0 ga bo'lish mumkin emas")
    return  f"Divison: {a / b}"

        
