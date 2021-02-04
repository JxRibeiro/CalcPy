a = 0
b = 0
op = 0

def soma(a, b):
    return a+b

def subtracao(a, b):
    return a-b

def divisao(a, b):
    return a/b

def multiplicacao(a, b):
    return a*b

a = float(input('Escolha um num: '))
b = float(input('Escolha outro num: '))
ope = input('Escolha uma operação: \n[A] Soma\n[B] Subtração\n[C] Divisão\n[D] Multiplicação\n')
op = ope.upper()
if op=='A':
    print(soma(a, b))
if op=='B':
    print(subtracao(a, b))
if op=='C':
    print(divisao(a, b))
if op=='D':
    print(multiplicacao(a, b))

