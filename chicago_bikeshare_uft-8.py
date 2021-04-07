# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
''' Constitui a variavel "data" para incluir os 21 primeiros registros, juntamente com o título.'''
for data in data_list[:21]:
    print(data)
# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]
# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for data in data_list[:20]:
    print(data[6])
# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros


input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
'''Função column_to_list.
   Argumentos: 
   column_list: Criação de lista vazia.
   i: variavel criada para oredenar os elementos da lista.
   data: elementos da lista.
   column_list.append(i[index]): inclui os elementos na nova lista, mantendo a ordem.
   Retorna:
   Os valores da coluna em uma lista, mantendo a ordem.'''
def column_to_list(data, index):
    column_list = []
    for i in data:
        column_list.append(i[index])
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0
'''Usando o looping "for", realiza a contagem de generos feminino e masculino. '''
for data in data_list:
    if data[-2] == 'Male':
        male += 1
    elif data[-2] == 'Female':
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
'''Função count_gender
   Argumentos:
   male: Variável utilizada para receber as ocorrencias verdadeiras do loop "for" para "Male".
   female: Variável utilizada para receber as ocorrencias verdadeiras do loop "for" para "Female".
   loop "for": realiza a verificação de cada linha com a condição "if", somando 1 para masculino quando "Male" e
   1 ao feminino quando "Female".
   Retorno:
   Retorna a contagem total de dumeros masculinos e femininos dentro da coluna [-2}
   '''

def count_gender(data_list):
    male = 0
    female = 0
    for data in data_list:
        if data[-2] == 'Male':
            male += 1
        elif data[-2] == 'Female':
            female += 1
    return [male, female]
print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
'''Função most_popular_gender
   Argumentos:
   answer: receberá a resposta como string
   male: Variável utilizada para receber as ocorrencias verdadeiras do loop "for" para "Male".
   female: Variável utilizada para receber as ocorrencias verdadeiras do loop "for" para "Female".
   loop "for": realiza a verificação de cada linha com a condição "if", somando 1 para masculino quando "Male" e
   1 ao feminino quando "Female".
   Condicional "if": compara qual registro é maior "Male" ou "Female".
   Retorna:
   Retorna a string que possui maior ocorrencia dentro da coluna [-2].
   '''
def most_popular_gender(data_list):
    answer = ""
    male = 0
    female = 0
    for data in data_list:
        if data[-2] == 'Male':
            male += 1
        elif data[-2] == 'Female':
            female += 1
    if female > male:
        answer = 'Feminino'
    elif female < male:
        answer = 'Masculino'
    elif female == male:
        answer = 'Igual'
    return answer

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

'''Função count_user_types
   Argumentos:
   customer: Variável utilizada para receber as ocorrencias verdadeiras do loop "for" para "Customer".
   subscriber: Variável utilizada para receber as ocorrencias verdadeiras do loop "for" para "Subscriber".
    loop "for": realiza a verificação de cada linha com a condição "if", somando 1 para customer quando "Customer" e
   1 ao subscriber quando "Subscriber".
   Retorno:
   Retorna a contagem total de ocorrencias "Customer" e "Subscriber" dentro da coluna [-3]
   '''

def count_user_types(data_list):
    customer = 0
    subscriber = 0
    for data in data_list:
        if data[-3] == 'Customer':
            customer += 1
        elif data[-3] == 'Subscriber':
            subscriber += 1
    return [customer, subscriber]

gender_list = column_to_list(data_list, -3)
user_types = ["Customer", "Subscriber"]
quantity = count_user_types(data_list)
y_pos = list(range(len(user_types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, user_types)
plt.title('Quantidade por Usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "O somatório de generos é diferente da contagem de linhas. A soma não registra os resultados diferentes de\n" \
         "'male' e 'female', ou seja, os registros vazios. Já a função realiza a contagem total de linhas, independente\n" \
         "do conteúdo. \n"
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

soma_trip_duration = 0
total_registro = 0
trip_duration_list_int = []

for trip_duration in trip_duration_list:
    trip_duration = int(trip_duration)
    trip_duration_list_int += [trip_duration]
    soma_trip_duration += trip_duration
    total_registro += 1
    if min_trip == 0 or min_trip > trip_duration:
        min_trip = trip_duration
    elif max_trip == 0 or max_trip < trip_duration:
        max_trip = trip_duration

mean_trip = soma_trip_duration / total_registro
trip_duration_list_int = sorted(trip_duration_list_int)
metade = total_registro // 2
median_trip = trip_duration_list_int[metade]


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
gender_list = column_to_list(data_list, -5)
user_types = set(gender_list)
print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

