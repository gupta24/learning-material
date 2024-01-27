def sum_value(summation):
    print("callable outer sum method..")
    def wrap(*args, **kwargs):
        if summation(*args):
            total = sum(args)
            return total
    return wrap


@sum_value
def check_args(*args):
    if args:
        return True
    return False

print(check_args(1,2,3,4,5))