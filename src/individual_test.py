import random
import numpy as np
from collections import Counter

'''
1- Caetano
2- Tadeu
3- Ermerson
4- Cesar
5- Jhon
6- Bruno
7- Priscilla
'''
'''
individual = np.array([
    [
        ['Sistemas Operacionais', 'Prof. Caetano Vieira', 1],
        ['Programação Procedural', 'Prof. Cicero Tadeu', 2],
        ['Desenvolvimento Web Front-End', 'Prof. José Ermerson', 3],
        ['CEV Universitária', 'Prof. Cesar Augusto', 4],
        ['Projeto Integrador: IoT', 'Prof. Jhonatta Pietro', 5]
    ],
    [
        ['Segurança e Auditoria de Sistemas', 'Prof. Caetano Vieira', 1],
        ['Operações em Banco de Dados', 'Prof. Cicero Tadeu', 2],
        ['Estatística', 'Prof. Bruno Barros', 6],
        ['Cultura e Sociedade', 'Profa. Priscilla Ribeiro', 7],
        ['PI: Sistemas Distribuídos', 'Prof. Caetano Vieira', 1]
    ],
    [
        ['Projeto e Desenvolvimento Web', 'Prof. Caetano Vieira', 1],
        ['Inteligência Artificial', 'Prof. Caetano Vieira', 1],
        ['Matemática aplicada à Data Science', 'Paulo Vinícius', 8],
        ['Empreendedorismo', 'Piedley Macedo Saraiva', 9],
        ['Projeto Integrador: Data Science and Big Data', 'Prof. Fabrício Carneiro', 2]
    ],
    [
        ['TCC II', 'Prof. Cesar Augusto', 4],
        ['Informática e Legislação', 'Prof. Caetano Vieira', 1],
        ['Estágio', 'Prof. José Ermerson', 3],
        ['Projeto Integrador: Tecnologias Emergentes', 'Prof. Fabrício Carneiro', 2],
        ['', '', 0]
    ]
])
'''

individual = np.array([[1, 2, 3, 4, 5],
                       [1, 2, 6, 7, 1],
                       [2, 1, 8, 9, 2],
                       [4, 1, 3, 2, 0]
                       ])
'''
for i in range(4):
    random.shuffle(individual[i])

for i in individual:
    for j, day in zip(i, ['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira']):
        print("{} - {}".format(day, j))
    print('---------------')
'''
# print(Counter(individual[:, 0]))
# print(round(sum([v for (k, v) in dict(Counter(individual[:, 0])).items() if v > 1]) / 2))

result = -1
n = 0

while result != 0:
    result = 0
    # Quantidade de semestres
    for i in range(4):
        random.shuffle(individual[i])

    # Dias da semana
    for i in range(5):
        counter = Counter(individual[:, i])
        amount = sum([v for (k, v) in dict(counter).items() if v > 1])
        result += round(amount / 2)
    n += 1
    print(result)
    print(individual)
    
print(n)

'''
result = -1

while result != 0:
    result = 0
    # Quantidade de semestres
    for i in range(4):
        random.shuffle(individual[i])

    # Dias da semana
    for i in range(5):
        counter = Counter(individual[:, i][:, 2])
        print(counter)
        amount = sum([v for (k, v) in dict(counter).items() if v > 1])
        result += round(amount / 2)
    print(result)
# print(individual[:, 1][:, [2]])
'''
'''
for i in range(4):
    random.shuffle(individual[i])
for i in individual:
    print(i)
'''
