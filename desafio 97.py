'''def escreva(str):
    s = 'º°'
    while len(s) < len(str):
        s += 'º°'
    print(s)
    print(str)
    print(s)'''



def escreva(str):
    tam = len(str) + 4
    print('°' * tam)
    print(f'  {str}')
    print('°' * tam)


escreva('Ola Mundo')
escreva('Sejam bem vindos!')
escreva('u know nothing, Jon Snow')