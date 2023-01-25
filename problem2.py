we_are_looking = 4 * 10 ** 6 # 4 million

def find_fib_sum(number_of):
    first = 1
    second = 1
    last = 0
    sum_fibs = 0

    while last < number_of:
        last = (first + second)

        if last % 2 == 0: # find even
            sum_fibs += last

        first = int(second)
        second = int(last)

    return sum_fibs

print(find_fib_sum(we_are_looking))
