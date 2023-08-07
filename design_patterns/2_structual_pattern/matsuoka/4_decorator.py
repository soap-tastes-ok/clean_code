import functools


def main():
    print(mean("0.1", 0.2, "0.3"))


# Decorateする関数
def float_args_and_return(function):
    @functools.wraps(function)
    def wrapper(*args, **kargs):
        args = [float(arg) for arg in args]
        return function(*args, **kargs)

    return wrapper


# Decorateされる関数
@float_args_and_return
def mean(first, second, *rest):
    numbers = (first, second) + rest
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    main()
