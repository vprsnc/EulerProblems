def multiples(range_):
    return (x for x in range(range_) if x % 3 == 0 \
        or x % 5 == 0)


def sum_multiples(range_):
    return sum(multiples(range_))


print(sum_multiples(1001))
