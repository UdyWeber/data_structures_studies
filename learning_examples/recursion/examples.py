def factorial(x: int):
    if x == 1:
        return x

    return x * (factorial(x - 1))


if __name__ == '__main__':
    print(factorial(4))
