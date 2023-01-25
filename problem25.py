fib = [0, 1]

iter_ = 2

#loop breaks when the number is 1000 digits long
while True:
    fib_new = fib[iter_ - 1] + fib[iter_ - 2]
    fib.append(fib_new)
    if fib_new > 10 ** 999:
        print(iter_)
        break
    iter_ += 1
