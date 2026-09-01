
Conversa com o Gemini
# 🍧 Sistema de Vendas - Açaíteria



Este projeto consiste em um sistema de gerenciamento e vendas baseado em terminal para uma Açaíteria, desenvolvido inteiramente em Python. O software visa organizar o catálogo de produtos, controlar estoque, aplicar regras de promoções diárias, processar pagamentos e registrar o histórico de vendas de forma simples e eficiente.

<!-- Esse projeto é meu -->

---



## 📌 Panoramas Gerais (Histórias de Usuário)



O desenvolvimento deste sistema foi guiado por diferentes perspectivas e necessidades de negócio:



* **👑 Product Owner (PO):** Necessita de um sistema de vendas centralizado para organizar os produtos da açaíteria, controlar o fluxo de saída de mercadorias e oferecer um atendimento rápido e ágil aos clientes.

* **👥 Quality Assurance / Cliente (QA):** Deseja um sistema transparente onde seja possível visualizar o menu de produtos, escolher o açaí ideal com seus respectivos adicionais, consultar informações da loja e realizar compras sem complicações.

* **💻 Tech / Programador:** Focado em criar um software estruturado, limpo, modular e de fácil manutenção utilizando os conceitos fundamentais da lógica de programação em Python.

* **🛠️ Developer (Dev):** Responsável por implementar regras de cadastro de produtos, listagem dinâmica, controle rigoroso de estoque, aplicação de cupons/descontos, e armazenamento do histórico de vendas.

* **🎨 UX Designer:** Preocupado em garantir uma interface de terminal simples, com menus numéricos de fácil navegação e retornos visuais amigáveis (emojis e resumos de pedidos) para o usuário.

* **📊 Analista de Dados (IA):** Busca coletar registros precisos sobre o volume de vendas, faturamento e as preferências de sabores/tamanhos mais pedidos para futuras tomadas de decisão na empresa.



---



## 🚀 Funcionalidades Principais



O sistema opera em um loop interativo (`while True`) com um menu composto por 10 opções:



1.  **Gerenciamento de Produtos:** Permite cadastrar dinamicamente até 3 produtos simultâneos no sistema (vagas limitadas no código atual), definindo nome, estoque inicial, preço, validade e descrição.

2.  **Listagem de Catálogo:** Exibe de forma organizada os detalhes de todos os produtos ativos e disponíveis no sistema.

3.  **Realização de Vendas:** Abate a quantidade desejada do estoque atual do produto, calcula o valor parcial e armazena os dados temporariamente.

4.  **Cardápio Interativo:** Menu interativo focado na experiência do cliente, permitindo selecionar o tamanho do açaí (*Tradicional, Premium ou Especial*) e os *toppings* adicionais (*Frutas, Granola, Paçoca ou Nutella*).

5.  **Módulo de Promoções:** Regras de negócio automatizadas por dia da semana:

    * *Terça do Tradicional:* 15% de desconto para compras acima de 2 unidades do açaí tradicional.

    * *Quinta Premium:* R$ 10,00 de desconto fixo no total.

    * *Combo Fim de Semana (Sex a Dom):* 10% de desconto em compras com valor total acima de R$ 90,00.

6.  **Formas de Pagamento:** Processamento de pagamentos com tratativas específicas:

    * **Pix:** Concede 5% de desconto automaticamente.

    * **Cartão (Crédito/Débito):** Valor integral da compra.

    * **Dinheiro:** Cálculo automático de troco. *(Inclui estorno automatizado de estoque caso a venda seja cancelada ou o valor pago seja insuficiente).*

7.  **Histórico de Vendas:** Exibe um relatório completo de todas as transações finalizadas com sucesso durante a execução do programa.

8.  **Modos de Entrega, Contato e Suporte:** Estruturas preparadas para exibição de informações da loja física e canais de atendimento.



---



## 🛠️ Tecnologias Utilizadas



O projeto foi construído utilizando recursos nativos da linguagem **Python 3**, sem a necessidade de instalação de bibliotecas externas:



* **Estruturas de Repetição e Condicionais:** `while`, `if`, `elif`, `else` para controle do fluxo do menu e validações.

* **Coleções de Dados:** * `Tuplas` para dados imutáveis (Tamanhos e Toppings).

    * `Listas` para dados dinâmicos (Dias da semana e Histórico de vendas).

    * `Dicionários` para mapeamento de dados estruturados (Preços promocionais e objetos de venda).

* **Funções (`def`):** Utilizadas para encapsular e modularizar a lógica do cálculo de descontos e promoções.

* **Formatação de Strings:** Uso de f-strings e formatadores numéricos (`:.2f`) para exibição monetária limpa.



---



## 🎮 Como Executar o Projeto



1. Certifique-se de ter o **Python 3.x** instalado em sua máquina.

2. Faça o clone deste repositório ou baixe o arquivo do código.

3. Abra o terminal na pasta do arquivo e execute o comando:

   ```bash

   python nome_do_seu_arquivo.py este é im exemplo de redme para o seguinte codigo preciso de outto sem parecer igual mas que mao falte o necessario

Aqui está uma versão completamente reescrita e reestruturada do README.md, mantendo todos os requisitos e informações necessárias, mas com uma linguagem, formatação e organização totalmente originais para evitar a sensação de cópia.

🍇 PDV & Gestão de Açaíteria em Python
Aplicação de Terminal (CLI) desenvolvida para automatizar vendas, aplicar ofertas diárias, controlar inventário e registrar transações em estabelecimentos comercializadores de açaí.

🎯 Objetivos do Projeto & Papéis do Sistema
A construção do software foi orientada por diferentes necessidades funcionais do negócio, atendendo a múltiplos perfis de partes interessadas (stakeholders):

Gestão do Negócio (Product Owner): Foco em centralizar a operação do caixa, otimizar o fluxo financeiro e agilizar o tempo de resposta durante o atendimento presencial.

Experiência do Consumidor (QA / Cliente): Interface transparente onde é possível navegar pelo catálogo, personalizar o açaí com acompanhamentos, checar dados do estabelecimento e fechar o pedido de forma intuitiva.

Arquitetura de Código (Tech Lead): Implementação de uma base sólida em Python puro, priorizando modularidade, facilidade de manutenção e legibilidade.

Engenharia de Software (Developer): Desenvolvimento dos módulos operacionais, incluindo cadastro de itens, controle dinâmico de saldo em estoque, validação de regras fiscais/descontos e persistência temporária de vendas.

Design de Interface (UX): Menus numéricos bem definidos, mensagens informativas com ícones visuais e resumos claros de cada etapa do pedido.

Inteligência de Dados (Analista de Dados): Consolidação de métricas operacionais (total faturado, itens mais comercializados e ticket médio) para embasamento de estratégias de mercado.

Estrutura de toppings e tamanhos suportados no cardápio, gerada com IA
Estrutura de toppings e tamanhos suportados no cardápio. Fonte: Sergio Amiti / Getty Images
⚙️ Módulos e Recursos do Sistema
O programa roda em loop dinâmico (while True) e oferece um painel principal com 10 funcionalidades distintas:

Módulo	Descrição Operacional
1. Cadastro de Produtos	Permite registrar até 3 itens simultaneamente no inventário (nome, quantidade em estoque, preço unitário, validade e descrição detalhada).
2. Consulta de Estoque	Apresenta o catálogo completo com a situação atual dos itens armazenados no sistema.
3. Fluxo de Vendas Direta	Processa a saída pontual de produtos cadastrados, abatendo o estoque e acumulando o valor da compra.
4. Cardápio de Açaí	Permite a montagem personalizada escolhendo o copo/tigela (Tradicional, Premium ou Especial) e os acompanhamentos (Frutas, Granola, Paçoca ou Nutella).
5. Motor de Promoções	
Aplica automaticamente descontos baseados no dia da semana:


• Terça-feira: 15% OFF em compras com +2 unidades do açaí Tradicional.


• Quinta-feira: Abatimento fixo de R$ 10,00 no subtotal.


• Sexta a Domingo: 10% OFF em pedidos que ultrapassarem R$ 90,00.

6. Check-out e Pagamento	
Processa o acerto financeiro através de três modalidades:


• Pix: Desconto automático de 5%.


• Cartão: Cobrança do valor líquido final.


• Dinheiro: Validação do valor entregue e cálculo de troco (com reversão de estoque automática se a transação for cancelada ou faltar valor).

7. Relatório de Transações	Exibe o histórico consolidados das vendas efetuadas na sessão.
8, 9 e 10. Suporte & Informações	Exibição de dados institucionais, localização e canais de atendimento da loja.
🧰 Especificações Técnicas
A solução utiliza estritamente recursos padrão do Python 3, eliminando a dependência de pacotes de terceiros:

Controle de Fluxo: Laços de repetição (while) e estruturas de decisão (if/elif/else) para navegação nos menus e validação de regras de negócio.

Estruturas de Dados:

Tuplas: Utilizadas para coleções fixas (ex: opções de toppings e tamanhos).

Listas: Utilizadas para dados mutáveis (ex: dias da semana e log de transações).

Dicionários: Utilizados para o mapeamento estruturado de entidades e regras financeiras.

Modularização: Uso extenso de funções (def) com retorno de valores e passagem de parâmetros.

Saída Formatada: Manipulação de texto com f-strings e formatação monetária padrão (R$ {:.2f}).

🚀 Como Testar e Executar
Requisito prévio: Python 3.x instalado.

Clone o repositório ou baixe o arquivo .py do projeto.

Abra o terminal de comandos no diretório do arquivo e execute:

Bash
python seu_codigo.py
'''

pensamento projeto seunome <-nome da pasta



Um Bloco de Comentarios.

Para explicar o que o código faz, ou para deixar anotações para o programador.

>>projeto açaiteria:



>PO (Como dono do negocio: Quero um sistema de vendas para minha açaiteria,

para que eu possa controlar as vendas e os produtos.)



>QA (Como cliente: Quero um sistema de vendas para minha açaiteria,

para que eu possa comprar meus produtos favoritos de forma rápida e fácil.)



>Tech (Como programador: Quero um sistema de vendas para minha açaiteria,

para que eu possa desenvolver um software eficiente e funcional para o negócio.)



>Dev (Como programador: Quero um sistema de vendas para minha açaiteria,

para que eu possa implementar as funcionalidades necessárias para

atender as necessidades do negócio e dos clientes.)



>UX (Como designer de experiência do usuário: Quero um sistema de

vendas para minha açaiteria,para que eu possa criar uma

interface intuitiva e agradável para os usuários,

garantindo uma experiência de compra satisfatória.)



>IA (Como analista de dados: Quero um sistema de vendas para minha

açaiteria, para que eu possa coletar e analisar os dados de vendas,

ajudando a identificar padrões de consumo e otimizar as

estratégias de marketing e estoque.)





Ciclo de vida do projeto:

1. Planejamento: Definir os requisitos do sistema, identificar as necessidades do negócio e dos clientes,

e criar um plano de desenvolvimento.

2. Análise: Analisar os requisitos e criar um modelo de dados e um design de sistema.

3. Desenvolvimento: Escrever o código para implementar as funcionalidades do sistema.

4. Testes: Testar o sistema para garantir que ele funcione corretamente e atenda aos requisitos.

5. Implantação: Implantar o sistema em um ambiente de produção e garantir que ele esteja funcionando

corretamente.

6. Manutenção: Realizar manutenção contínua para corrigir bugs, adicionar novas funcionalidades e garantir

que o sistema continue atendendo às necessidades do negócio e dos clientes.



>>Criar um aplicativo, sistema em CLI - Command Line Interface, ou seja, um sistema que funcione no terminal, sem interface gráfica.

>>Complementar e implementar o app / sistema em GUI - Graphical User Interface, ou seja, um sistema com interface gráfica,

para que os usuários possam interagir de forma mais intuitiva e agradável.



'''

# Inicializando as variáveis para o Produto 1 (vazio)

p1_nome = "açaí comum"

p1_estoque = 100

p1_preco = 8.90

p1_validade = "10/12/2026"

p1_descricao = "Açaí comum, ideal para quem gosta de um sabor clássico."



# Preciso criar um dicionário para o produto 1, mas não sei como fazer isso ainda.

# produto_p1 = {

#     "p1_nome": "açaí comum",

#     "p1_estoque": p1_estoque,

#     "p1_preco": p1_preco,

#     "p1_validade": p1_validade,

#     "p1_descricao": p1_descricao

# }



# Inicializando as variáveis para o Produto 2 (vazio)

p2_nome = "açaí guarana"

p2_estoque = 50

p2_preco = 12.90

p2_validade = "10/10/2026"

p2_descricao = "Açaí guarana, com sabor refrescante e ingredientes de qualidade."



# Inicializando as variáveis para o Produto 3 (vazio)

p3_nome = "açaí cupuaçu"

p3_estoque = 130

p3_preco = 15.90

p3_validade = "10/12/2026"

p3_descricao = "Açaí cupuaçu, com ingredientes locais e sabor autêntico."



# Isso é um comentário de linha única.



while True:

    print('-' * 48 + '\n')

    print('Bem-vindo ao Sistema de vendas - açaiteria!\n')

    print('1 - Cadastrar produto')

    print('2 - Listar produtos')

    print('3 - Realizar venda')

# cardapio; forma de pagamento; contato-empresa; historico de vendas;

## modo de entrega; suporte;



    print('0 - Sair')

    print('\n--------------------------------------\n')



    opcao = input('Digite a opção desejada: ')



    if opcao == '1':

        print('Cadastrando produtos...\n')

    # faça a lógica para cadastrar o produto aqui,

    ## e somente a inseção dos dados usando input e os tipos de dados.

        if p1_nome == "":

            p1_nome = input('Digite o nome do produto: ')

            p1_estoque = int(input('Digite a quantidade em estoque: '))

            p1_preco = float(input('Digite o preço do produto: '))

            p1_validade = input('Digite a validade do produto: ')    

            p1_descricao = input('Digite a descrição do produto: ')

            print(f'\n🎉 Produto "{p1_nome}" cadastrado na vaga 1!')          

        elif p2_nome == "":

                p2_nome = input('Digite o nome do produto: ')

                p2_estoque = int(input('Digite a quantidade em estoque: '))

                p2_preco = float(input('Digite o preço do produto: '))

                p2_validade = input('Digite a validade do produto: ')    

                p2_descricao = input('Digite a descrição do produto: ')

                print(f'\n🎉 Produto "{p2_nome}" cadastrado na vaga 2!')      

        elif p3_nome == "":

            p3_nome = input('Digite o nome do produto: ')

            p3_estoque = int(input('Digite a quantidade em estoque: '))

            p3_preco = float(input('Digite o preço do produto: '))

            p3_validade = input('Digite a validade do produto: ')    

            p3_descricao = input('Digite a descrição do produto: ')

            print(f'\n🎉 Produto "{p3_nome}" cadastrado na vaga 3!')

           

        else:

            print('❌ Sistema cheio! Limite de 3 produtos atingido.')



    elif opcao == '2':

        print('Listando produtos...')



        if p1_nome == "" and p2_nome == "" and p3_nome == "":



            print('Nenhum produto cadastrado no sistema ainda.')



        else:

            # Mostra o Produto 1 se ele existir

            if p1_nome != "":

                print(f"Nome: {p1_nome} | Preço: R$ {p1_preco:.2f} | Estoque: {p1_estoque} unid.")



                print(f"Validade: {p1_validade} | Descrição: {p1_descricao}")



                print('🔥' * 30)

               

            # Mostra o Produto 2 se ele existir

            if p2_nome != "":



                print(f"Nome: {p2_nome} | Preço: R$ {p2_preco:.2f} | Estoque: {p2_estoque} unid.")



                print(f"Validade: {p2_validade} | Descrição: {p2_descricao}")



                print('🔥' * 30)

               

            # Mostra o Produto 3 se ele existir

            if p3_nome != "":



                print(f"Nome: {p3_nome} | Preço: R$ {p3_preco:.2f} | Estoque: {p3_estoque} unid.")



                print(f"Validade: {p3_validade} | Descrição: {p3_descricao}")



                print('🔥' * 30)



    elif opcao == '3':

        print('Realizando venda...')



        if p1_nome == "" and p2_nome == "" and p3_nome == "":

            print(f'Não há produtos cadastrados para realizar vendas.')

        else:

            nome_venda = input('Digite o nome do produto que deseja vender: ')

           

            # Testamos o nome digitado contra o Produto 1

            if nome_venda.lower() == p1_nome.lower() and p1_nome != "":

                qtd_venda = int(input(f"Quantas unidades de '{p1_nome}' deseja vender? "))

                if qtd_venda <= p1_estoque:

                    p1_estoque -= qtd_venda

                    total = qtd_venda * p1_preco

                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')

                    print(f'Estoque atual de {p1_nome}: {p1_estoque} unidades.')

                else:

                    print(f'❌ Estoque insuficiente! Temos apenas {p1_estoque}.')

           

            # Testamos contra o Produto 2

            elif nome_venda.lower() == p2_nome.lower() and p2_nome != "":

                qtd_venda = int(input(f"Quantas unidades de '{p2_nome}' deseja vender? "))

                if qtd_venda <= p2_estoque:

                    p2_estoque -= qtd_venda

                    total = qtd_venda * p2_preco

                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')

                    print(f'Estoque atual de {p2_nome}: {p2_estoque} unidades.')

                else:

                    print(f'❌ Estoque insuficiente! Temos apenas {p2_estoque}.')

                   

            # Testamos contra o Produto 3

            elif nome_venda.lower() == p3_nome.lower() and p3_nome != "":

                qtd_venda = int(input(f"Quantas unidades de '{p3_nome}' deseja vender? "))

                if qtd_venda <= p3_estoque:

                    p3_estoque -= qtd_venda

                    total = qtd_venda * p3_preco

                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')

                    print(f'Estoque atual de {p3_nome}: {p3_estoque} unidades.')

                else:

                    print(f'❌ Estoque insuficiente! Temos apenas {p3_estoque}.')

           

            else:

                print('🔥 Erro: Produto não encontrado!')



    elif opcao == '0':

        print('Saindo...')

        break

    else:

        print('Opção inválida!')

Aqui está uma proposta completa e reestruturada de README.md para o seu repositório. O texto cobre todas as funcionalidades e intenções contidas no seu código Python, mas com uma linguagem, formatação e títulos totalmente inéditos.

🍇 PDV Terminal — Gestão & Vendas de Açaí
Sistema em linha de comando (CLI) desenvolvido em Python para operacionalizar as vendas, controlar o estoque físico e oferecer atendimento dinâmico em estabelecimentos de açaí.

👥 Visão Multidisciplinar (Perspectivas do Projeto)
O alinhamento do software baseou-se nos objetivos de diferentes papéis da equipe e do negócio:

Visão de Negócio (PO): Centralizar as rotinas de caixa e catálogo para acelerar o atendimento e mitigar perdas de estoque.

Foco no Usuário (QA / Consumidor): Garantir um fluxo de escolha claro, com consulta transparente de preços, acompanhamentos e totalizadores.

Arquitetura (Tech Lead): Construir uma base lógica em Python puro, focada na legibilidade do código e facilidade para futuras refatorações.

Implementação (Dev): Desenvolver validações de entrada, abatimento em tempo real do estoque e rotinas de liquidação financeiras.

Interface (UX): Construir menuações numeradas de rápida leitura e mensagens com símbolos visuais no terminal.

Análise (Analista de Dados): Consolidar informações das vendas efetuadas para acompanhamento de faturamento e preferências do público.

🛠️ Recursos e Funcionalidades
A aplicação roda em um loop contínuo (while True), agrupando 10 opções operacionais:

Inclusão de Produtos: Permite incluir até 3 itens dinâmicos com controle de lote, valor, quantidade inicial e descrição.

Consulta do Catálogo: Apresentação visual detalhada das mercadorias ativas no estoque.

Baixa e Venda Direta: Abatimento automático de unidades em estoque e cálculo instantâneo do valor da venda.

Customização de Pedidos: Seleção de tamanhos (Tradicional, Premium, Especial) e acréscimo de coberturas/adicionais (Frutas, Granola, Paçoca, Nutella).

Automação de Descontos Diários:

Terça: 15% de abatimento em pedidos com 2+ açaís tradicionais.

Quinta: R$ 10,00 de desconto direto no subtotal.

Fim de Semana (Sex-Dom): 10% OFF em consumos acima de R$ 90,00.

Formas de Liquidação:

Pix: Concede 5% de desconto automático.

Cartões: Débito e crédito com cobrança de valor integral.

Espécie: Cálculo automatizado de troco (com estorno de produtos caso a transação não seja concluída).

Relatório de Transações: Registro das operações finalizadas ao longo do ciclo de execução.

Informações Gerais: Endereço, modalidades de entrega e suporte ao cliente.

💻 Estrutura Técnica
Construído sem dependência de módulos externos, utilizando apenas recursos nativos da linguagem Python 3:

Controle de Fluxo: Laços de repetição (while) e blocos de validação condicional (if / elif / else).

Estruturas de Coleção:

Tuplas: Manipulação de listas imutáveis (como opções de adicionais).

Listas: Armazenamento dinâmico do histórico de operações e dias da semana.

Dicionários: Mapeamento estruturado de propriedades e produtos.

Funções Customizadas: Encapsulamento de rotinas para cálculo financeiro e regras promocionais.

Formatação de Saída: Uso de f-strings e formatadores de decimais (:.2f).

🚀 Como Executar a Aplicação
Certifique-se de possuir o Python 3 instalado em seu sistema.

Baixe o código fonte do repositório.

Execute no terminal:

Bash
python seu_arquivo.py
Gere o código fonte completo do arquivo README.md para eu copiar diretamente.

"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(readme_content)

print("README.md gerado com sucesso!")


```text?code_stdout&code_event_index=1
README.md gerado com sucesso!

Seu arquivo README.md foi gerado. Você pode baixá-lo diretamente ou copiar o código-fonte Markdown abaixo:

Ícone do app MD
README
 MD 
Markdown
# 🍇 PDV Terminal — Gestão & Vendas de Açaí

Sistema em linha de comando (CLI) desenvolvido em Python para operacionalizar as vendas, controlar o estoque físico e oferecer atendimento dinâmico em estabelecimentos de açaí.

---

## 👥 Visão Multidisciplinar (Perspectivas do Projeto)

O alinhamento do software baseou-se nos objetivos de diferentes papéis da equipe e do negócio:

* **Visão de Negócio (PO):** Centralizar as rotinas de caixa e catálogo para acelerar o atendimento e mitigar perdas de estoque.
* **Foco no Usuário (QA / Consumidor):** Garantir um fluxo de escolha claro, com consulta transparente de preços, acompanhamentos e totalizadores.
* **Arquitetura (Tech Lead):** Construir uma base lógica em Python puro, focada na legibilidade do código e facilidade para futuras refatorações.
* **Implementação (Dev):** Desenvolver validações de entrada, abatimento em tempo real do estoque e rotinas de liquidação financeiras.
* **Interface (UX):** Construir menuações numeradas de rápida leitura e mensagens com símbolos visuais no terminal.
* **Análise (Analista de Dados):** Consolidar informações das vendas efetuadas para acompanhamento de faturamento e preferências do público.

---

## 🛠️ Recursos e Funcionalidades

A aplicação roda em um loop contínuo (`while True`), agrupando **10 opções operacionais**:

1. **Inclusão de Produtos:** Permite incluir até 3 itens dinâmicos com controle de lote, valor, quantidade inicial e descrição.
2. **Consulta do Catálogo:** Apresentação visual detalhada das mercadorias ativas no estoque.
3. **Baixa e Venda Direta:** Abatimento automático de unidades em estoque e cálculo instantâneo do valor da venda.
4. **Customização de Pedidos:** Seleção de tamanhos (*Tradicional, Premium, Especial*) e acréscimo de coberturas/adicionais (*Frutas, Granola, Paçoca, Nutella*).
5. **Automação de Descontos Diários:**
   * **Terça:** 15% de abatimento em pedidos com 2+ açaís tradicionais.
   * **Quinta:** R$ 10,00 de desconto direto no subtotal.
   * **Fim de Semana (Sex-Dom):** 10% OFF em consumos acima de R$ 90,00.
6. **Formas de Liquidação:**
   * **Pix:** Concede 5% de desconto automático.
   * **Cartões:** Débito e crédito com cobrança de valor integral.
   * **Espécie:** Cálculo automatizado de troco (com estorno de produtos caso a transação não seja concluída).
7. **Relatório de Transações:** Registro das operações finalizadas ao longo do ciclo de execução.
8. **Informações Gerais:** Endereço, modalidades de entrega e suporte ao cliente.

---

## 💻 Estrutura Técnica

Construído sem dependência de módulos externos, utilizando apenas recursos nativos da linguagem **Python 3**:

* **Controle de Fluxo:** Laços de repetição (`while`) e blocos de validação condicional (`if / elif / else`).
* **Estruturas de Coleção:**
  * **Tuplas:** Manipulação de listas imutáveis (como opções de adicionais).
  * **Listas:** Armazenamento dinâmico do histórico de operações e dias da semana.
  * **Dicionários:** Mapeamento estruturado de propriedades e produtos.
* **Funções Customizadas:** Encapsulamento de rotinas para cálculo financeiro e regras promocionais.
* **Formatação de Saída:** Uso de *f-strings* e formatadores de decimais (`:.2f`).

---

## 🚀 Como Executar a Aplicação

1. Certifique-se de possuir o **Python 3** instalado em seu sistema.
2. Baixe o código fonte do repositório.
3. Execute no terminal:

```bash
python seu_arquivo.py



O Gemini não é humano. Ele pode cometer erros. Por isso, cheque as respostas.

Analisando
# 🍇 PDV Terminal — Gestão & Vendas de Açaí

Sistema em linha de comando (CLI) desenvolvido em Python para operacionalizar as vendas, controlar o estoque físico e oferecer atendimento dinâmico em estabelecimentos de açaí.

---

## 👥 Visão Multidisciplinar (Perspectivas do Projeto)

O alinhamento do software baseou-se nos objetivos de diferentes papéis da equipe e do negócio:

* **Visão de Negócio (PO):** Centralizar as rotinas de caixa e catálogo para acelerar o atendimento e mitigar perdas de estoque.
* **Foco no Usuário (QA / Consumidor):** Garantir um fluxo de escolha claro, com consulta transparente de preços, acompanhamentos e totalizadores.
* **Arquitetura (Tech Lead):** Construir uma base lógica em Python puro, focada na legibilidade do código e facilidade para futuras refatorações.
* **Implementação (Dev):** Desenvolver validações de entrada, abatimento em tempo real do estoque e rotinas de liquidação financeiras.
* **Interface (UX):** Construir menuações numeradas de rápida leitura e mensagens com símbolos visuais no terminal.
* **Análise (Analista de Dados):** Consolidar informações das vendas efetuadas para acompanhamento de faturamento e preferências do público.

---

## 🛠️ Recursos e Funcionalidades

A aplicação roda em um loop contínuo (`while True`), agrupando **10 opções operacionais**:

1. **Inclusão de Produtos:** Permite incluir até 3 itens dinâmicos com controle de lote, valor, quantidade inicial e descrição.
2. **Consulta do Catálogo:** Apresentação visual detalhada das mercadorias ativas no estoque.
3. **Baixa e Venda Direta:** Abatimento automático de unidades em estoque e cálculo instantâneo do valor da venda.
4. **Customização de Pedidos:** Seleção de tamanhos (*Tradicional, Premium, Especial*) e acréscimo de coberturas/adicionais (*Frutas, Granola, Paçoca, Nutella*).
5. **Automação de Descontos Diários:**
   * **Terça:** 15% de abatimento em pedidos com 2+ açaís tradicionais.
   * **Quinta:** R$ 10,00 de desconto direto no subtotal.
   * **Fim de Semana (Sex-Dom):** 10% OFF em consumos acima de R$ 90,00.
6. **Formas de Liquidação:**
   * **Pix:** Concede 5% de desconto automático.
   * **Cartões:** Débito e crédito com cobrança de valor integral.
   * **Espécie:** Cálculo automatizado de troco (com estorno de produtos caso a transação não seja concluída).
7. **Relatório de Transações:** Registro das operações finalizadas ao longo do ciclo de execução.
8. **Informações Gerais:** Endereço, modalidades de entrega e suporte ao cliente.

---

## 💻 Estrutura Técnica

Construído sem dependência de módulos externos, utilizando apenas recursos nativos da linguagem **Python 3**:

* **Controle de Fluxo:** Laços de repetição (`while`) e blocos de validação condicional (`if / elif / else`).
* **Estruturas de Coleção:**
  * **Tuplas:** Manipulação de listas imutáveis (como opções de adicionais).
  * **Listas:** Armazenamento dinâmico do histórico de operações e dias da semana.
  * **Dicionários:** Mapeamento estruturado de propriedades e produtos.
* **Funções Customizadas:** Encapsulamento de rotinas para cálculo financeiro e regras promocionais.
* **Formatação de Saída:** Uso de *f-strings* e formatadores de decimais (`:.2f`).

---

## 🚀 Como Executar a Aplicação

1. Certifique-se de possuir o **Python 3** instalado em seu sistema.
2. Baixe o código fonte do repositório.
3. Execute no terminal:

```bash
python seu_arquivo.py
```
README.md
Exibindo README.md.