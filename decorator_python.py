def repeat(n):
    def logging_decorator(genuine_function):
        def fake_function(x):
            if n == 0:
                result = x
            else:
                for i in range (0, n):
                    result = genuine_function(x)
                    x = result
                return x
            return result
        return fake_function
    return logging_decorator

@repeat(2)
def plus_1(x):
    return x + 1

@repeat(0)
def mul_2(x):
    return x * 2

print(plus_1(3))  # должно выдать 5
print(mul_2(4))  # должно выдать 4
