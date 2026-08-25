
# Permite trabalhar com data e horário
from datetime import datetime

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
