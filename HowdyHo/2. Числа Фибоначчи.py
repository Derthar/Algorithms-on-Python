
target = 25

# fib = [0] * target
# fib[0] = fib[1] = 1

fib = [1, 1]
ind = 2
x = 12

while ind < target:
    fib.append(fib[ind-1] + fib[ind-2])
    # fib[ind] = fib[ind-1] + fib[ind-2]
    ind += 1

print(fib[x])