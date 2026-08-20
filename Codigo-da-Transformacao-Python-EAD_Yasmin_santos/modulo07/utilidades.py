'''
Operações aritmeticas:

Divisão
Soma
Subtração
Porcentagem
Multiplicação

'''
def soma(a,b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def porcentagem(a, b):
    return a % b

def dividir(a, b):
    if b == 0:
      return "Erro: Divisão por zero ão permitida"
    return a / b

def divisao_inteira(a, b):
    '''
    Retorna apenas a parte inteira da divisão de 'a' poor 'b'.
    pârametros: a (int/float), b (int/float)
    Retorno: O quociente inteiro ou uma mensagem de erro se b == 0.    
    '''
    if b == 0:
      return "Erro: Divisão por zero não é permitida"
    return a // b

def resto_divisao(a, b):
    '''
    Calcule o resto da divisão ou mensagem de erro se b == 0.
    pârametros: a (int/float), b (int/float)
    Retorno: O quociente inteiro ou uma mensagem de erro se b == 0.    
    '''

    if b == 0:
      return "Erro: Divisão por zero não é permitida"
    return a % b

def portencia(base, expoente):
    return base ** expoente



def calcular_media(lista_numeros):

    if not lista_numeros:
      return 0
    return sum(lista_numeros) / len(lista_numeros)

    def e_par(numeros):
     return numero % 2 == 0

