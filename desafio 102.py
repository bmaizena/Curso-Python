def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end=' ')
            print('x' if c > 1 else '=', end=' ')
        f *= c
    return f

print(fatorial(9, True))