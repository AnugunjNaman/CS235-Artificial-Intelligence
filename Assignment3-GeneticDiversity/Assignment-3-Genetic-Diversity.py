
import random
from random import randint

random.seed(2)

def fitness(marks, n, chrom):
    j, p, b, c, fit = 0, 0, 0, 0, 0
    for i in range(n):
        p = abs(marks[i] - chrom[0])
        b = abs(marks[i] - chrom[1])
        c = abs(marks[i] - chrom[2])
        if p > b:
            if b > c:
                fit = fit + c
            else: 
                fit = fit + b
        else:
            if p > c:
                fit = fit + c
            else:
                fit = fit + p
    
    chrom[3] = fit



def chromosome(marks, n, population, m):
    i, j, k = 0, 0, 0
    for i in range(m):
        for j in range(3):
            k = randint(0, n - 1)
            population[i][j] = marks[k]

    for i in range(m):
        fitness(marks, n, population[i]) 


def sel_cross_mut(marks, n, population, m):
    _population = [[0]*4]*50
    i, t, k, j, w = 0, 0, 0, 0, 0
    for i in range(int(m/2)):
        maxi = 0
        for t in range(20):
            w = randint(0, m - 1)
            if(population[w][3] > maxi):
                maxi = population[w][3]
                k = w
        
        maxi = 0
        for t in range(20):
            w = randint(0, m - 1)
            if(population[w][3] > maxi):
                maxi = population[w][3]
                j = w

        c = randint(0, 2)
        for t in range(0, c + 1):
            _population[i][t] = population[k][t]
            _population[m-i-1][t] = population[j][t]
        
        for t in range(c + 1, 3):
            _population[i][t] = population[j][t]
            _population[m-i-1][t] = population[k][t]

    y = randint(0, m - 1)
    for i in range(y):
        g, h , r = (randint(0, m - 1), randint(0, 2), randint(0, n - 1))
        _population[g][h] = marks[r]

    for i in range(m):
        fitness(marks, n, _population[i]) 

    for i in range(m):
        for t in range(4):
            population[i][t] = _population[i][t]




n = 10
marks = []
for _ in range(n):
    marks.append(randint(1, 101))

rows, columns = (50, 4)
population = [[0]*columns]*rows

chromosome(marks, n, population, 50)

gmi, itr, mi = 99999999, 2000, 99999999
gminimum = [0]*4

while itr != 0 or (mi - gmi) > 0:
    itr = itr - 1
    minimum = [0]*4
    for i in range(50):
        if population[i][3] < mi:
            mi = population[i][3]
            minimum[0] = population[i][0]
            minimum[1] = population[i][1]
            minimum[2] = population[i][2]
            minimum[3] = population[i][3]

    if mi < gmi:
        gmi = mi
        gminimum[0] = minimum[0]
        gminimum[1] = minimum[1]
        gminimum[2] = minimum[2]
        gminimum[3] = minimum[3]

    sel_cross_mut(marks, n, population, 50)

g1, g2, g3 = ([], [], [])
for j in range(n):
    p =  abs(marks[j]-gminimum[0])
    b =  abs(marks[j]-gminimum[1])
    c =  abs(marks[j]-gminimum[2])
    if p > b:
        if b > c:
            g3.append(tuple((marks[j], j)))
        else: 
            g2.append(tuple((marks[j], j)))
    else:
        if p > c:
            g3.append(tuple((marks[j], j)))
        else:
            g1.append(tuple((marks[j], j)))


print('Group 1: ', gminimum[0])  
for i in g1:
    print(f'Student {i[1]} : {i[0]}')

print() 
print('Group 2: ', gminimum[1]) 
for i in g2:
    print(f'Student {i[1]} : {i[0]}')

print()   
print('Group 3: ', gminimum[2])  
for i in g3:
    print(f'Student {i[1]} : {i[0]}')

print() 
print('Fitness: ', gminimum[3]) 
