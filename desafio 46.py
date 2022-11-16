from time import sleep
print ('\033[31mA CONTAGEM REGRESSIVA IRÁ SE INICIAR EM:\033[31m')
sleep(2)
for c in range(10, -1, -1):
    print (c)
    sleep(0.5)
print ('\033[31mBOOOOM!!\033[m')
