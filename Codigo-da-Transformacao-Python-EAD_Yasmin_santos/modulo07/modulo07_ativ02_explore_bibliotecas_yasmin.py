import datetime
from faker import Faker
import utilidades

fake = Faker('pt_BR')

print('*** Dados Criados - Prova de Português***')
print(f'Nome de Mentira: {fake.name()}')
print(f'E-Mail de Mentira: {fake.email()}')
print(f'Telefone de Mentira: {fake.phone_number()}')

print('\n*** Dados da Prova de Mentira ***')
agora = datetime.datetime.now()
# Correção nas aspas da f-string para evitar erros de sintaxe
print(f'Data e hora atual: {agora.strftime("%H:%M %d/%m/%Y")}')

print('\n--- QUESTÃO 1 ---')
print('Qual das opções abaixo apresenta apenas palavras oxítonas?')
print('a) Mesa, cadeira, janela')
print('b) Café, caju, jacaré')
print('c) Lâmpada, óculos, árvore')

# Coleta a resposta do usuário convertendo para letras minúsculas (.lower())
resposta_usuario = input('Escolha sua alternativa (a, b ou c)?').strip().lower()

# Validação da resposta correta (A alternativa correta é a letra 'b')
if resposta_usuario == 'b':
    print('✅ Resposta CORRETA! Parabéns.✨')
else:
    print('❌ Resposta INCORRETA!. A alternativa correta era a letra (b).😔')

'''
num1 = 10
num2 = 5

print(f'Números utilizados: {num1} e {num2}')

print(f'Usando Adição ({num1} + {num2}):', utilidades.soma(num1, num2))
print(f'Usando Subtrair ({num1} - {num2}):', utilidades.subtrair(num1, num2))
print(f'Multiplicação ({num1} * {num2}):', utilidades.multiplicar(num1, num2))
print(f'Divisão ({num1} / {num2}):', utilidades.dividir(num1, num2))
print(f'Divisão Inteira ({num1} // {num2}):', utilidades.divisao_inteira(num1, num2))
print(f'Resto da Divisão ({num1} % {num2}):', utilidades.resto_divisao(num1, num2))
print(f'Potenciação ({num1} ** {num2}):', utilidades.potencia(num1, num2))

print("\n=== TESTE DE SEGURANÇA (DIVISÃO POR ZERO) ===")
print("Divisão por zero:", utilidades.dividir(10, 0))
'''