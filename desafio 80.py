num = []
for c in range(0,5):
    n = int(input('Digite um valor?'))
    if c == 0:
        num.append(n)
        print('adicionado ao final da lista')
    elif n > num[-1]:
        num.append(n)
        print ('adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'adicionado na posição {pos}')
                break
            pos +=1
print (f'os valores digitados em ordem foram {num}')