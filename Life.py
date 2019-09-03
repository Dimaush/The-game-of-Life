# Обозначения:
# # — скала
# € — рыба
# ~ — креветка
# curr — массив текущего состояния
# next — массив следующего состояния

import random
import os
import time

def check(i, j):
    S = [0, 0]
    for p in range (3):
        for q in range (3):
            if p != 1 or q != 1:
                g = curr[i + p - 1][j + q - 1]
                if g == '€': S[0] += 1
                elif g == '~': S[1] += 1
    return S

def step():
    global curr
    for i in range (n + 2): print(*next[i])
    curr = next[:]

# Очистка консоли
os.system('clear')

# Задание стороны моря
n = 10

next = [0] * (n + 2)
for i in range (n + 2): next[i] = [' '] * (n + 2)

# Генерация начального положения
for i in range (1, n + 1):
    for j in range (1, n + 1):
        x = random.randint (0, 3)
        if x == 0: next[i][j] = '#'
        elif x == 1: next[i][j] = ' '
        elif x == 2: next[i][j] = '€'
        else: next[i][j] = '~'

step()

while True:
    
    for i in range (1, n + 1):
        for j in range (1, n + 1):
            
            S = check(i, j)
            g = curr[i][j]
            
            # Проверка живой клетки на смерть
            if g == '€':
                if S[0] < 2 or S[0] > 3: next[i][j] = ' '
            elif g == '~':
                if S[1] < 2 or S[1] > 3: next[i][j] = ' '
    
    for i in range (1, n + 1):
        for j in range (1, n + 1):
            
            S = check(i, j)
            g = curr[i][j]
            
            # Проверка мёртвой клетки на жизнь
            if g == ' ':
                if S[0] == 3: next[i][j] = '€'
                elif S[1] == 3: next[i][j] = '~'
    
    time.sleep(10)
    os.system('clear')
    
    step()