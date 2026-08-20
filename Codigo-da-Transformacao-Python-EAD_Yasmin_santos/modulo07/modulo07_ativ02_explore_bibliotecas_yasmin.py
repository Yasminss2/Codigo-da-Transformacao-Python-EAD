'''
Programador: As variaáveis,serão inseridas no app - BACK-End
Dev: existe a interação com o usuario _ Web Design (front-end)
'''

# import utilidades

import utilidades
import datetime
from faker import Faker

fake = Faker('pt_BR')

'''
Faker é uma biblioteca de origem Coreana 😮✨🤞
'''

print('***Dados Criados - Prova de Matemática***')
print(f'Nome de Mentira: {fake.name()}')
print(f'Email de Mentira: {fake.email()}')
print(f'Telefone de Mentira: {fake.phone.number()}')


print(f'Dados da provaa de mentira ***')
agora = datetime.datetime.now()
print(f'Sua prova foi concluida: (agora.strftime('%d/%m/%Y'))')


num1 = 10
num2 = 5

print('🎀✨Testee de Utilidades✨🎀')
print(f'Numeros Utilizados: {num1} e {num2}')

# print(f' Adição ({num1 + num2}):', utilidades.soma{num1, num2})

# print(f'Teste adição({num1} + {num2}) :', utilidades.soma{num1, num2})

print(f'Mais teste ({num1} + {num2}) :', utilidades.soma(num1, num2))

# print(f' Subtrair({num1 - num2}):', utilidades.subtrair{num1, num2})
# print(f' Multiplicação ({num1 * num2}):', utilidades.multiplicar{num1, num2})
# print(f' Divisão ({num1 / num2}):', utilidades.dividir{num1, num2})
# print(f' Divisão Inteira ({num1 // num2}):', utilidades.divisao_inteira{num1, num2})
# print(f' Resto de divisão ({num1 % num2}):', utilidades.resto_divisao{num1, num2})
# print(f' Potenciação ({num1 ^ num2}):', utilidades.potencia{num1, num2})

# print("\n==== Teste e segurança (Divisão por zero) ===")
# print ("Divisão por zero:", utilidades.dividir(10, 0))
