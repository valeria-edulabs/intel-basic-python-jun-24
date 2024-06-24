def calc_control_digit(digits: str):
    total = 0
    weights = [1,2,1,2,1,2,1,2]
    for w, d in zip(weights, digits):
        mul = w * int(d)
        div, mod = divmod(mul, 10)
        mul = div + mod
        total += mul
        # total += sum(divmod(w * int(d), 10))
    return (10 - (total % 10)) % 10

def my_foo():
    print("foo")

print("**************************")
# control_dig = calc_control_digit("11111111")
# print(control_dig)
# def calc_control_digit(digits: list[int]):
#     pass