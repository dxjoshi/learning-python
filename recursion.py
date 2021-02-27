def power(number, pow):
    if pow == 0:
        return 1
    else:
        return number * power(number, pow - 1)


def factorial(number):
    if number < 0:
        raise ValueError('Number cannot be negative!!')
    if not number:
        return 1
    else:
        return number * factorial(number - 1)


print("2^5 is %d" % power(2, 5))
print("5! is %d" % factorial(5))
