import numpy as np
from Bio import SeqIO
import sys

argument1 = sys.argv[1]
argument2 = sys.argv[2]

match = int(sys.argv[3])
missmatch = int(sys.argv[4])
gap = int(sys.argv[5])



for record in SeqIO.parse(argument1, "fasta"):
    sekwencja = record.seq
for record in SeqIO.parse(argument2, "fasta"):
    sekwencja1 = record.seq

slowo1 = sekwencja
slowo2 = sekwencja1

matrix = np.zeros((len(slowo2) + 1, len(slowo1) + 1))
i=-0
j=-0

#inicjacja matrixa
for x in range(len(slowo1)+1):
    matrix[0][x] = i
    i -= 1

for x in range(len(slowo2)+1):
    matrix[x][0] = j
    j -= 1

#wypelnianie wartosciami
for row in range(1, len(slowo2)+1):
    for value in range(1, len(slowo1)+1):
        if slowo2[row-1] == slowo1[value-1]:
            matrix[row][value] = max(matrix[row-1][value-1]+match, matrix[row][value-1]-gap, matrix[row-1][value]-gap)
        else:
            matrix[row][value] = max(matrix[row-1][value-1]-missmatch, matrix[row][value-1]-gap, matrix[row-1][value]-gap)

wynik1=""
wynik2=""

column = len(slowo1)
row = len(slowo2)

score = 0

#odczytywanie i wynik
while row > 0 and column > 0:
    left = matrix[row][column-1]
    up = matrix[row-1][column]
    diag = matrix[row-1][column-1]

    if max(left, up, diag) == up:

        wynik1 += "-"
        wynik2 += slowo2[row-1]
        row -= 1
        score -= gap


    elif max(left, up, diag) == diag:
        wynik1 += slowo1[column-1]
        wynik2 += slowo2[row-1]
        column -= 1
        row -= 1
        if(slowo1[column-1] == slowo2[row-1]):
            score += match
        else:
            score -= missmatch

    else:
        wynik1 += slowo1[column-1]        
        wynik2 += "-"                     
        column -= 1
        score -= gap

print(score)

reversed1 = ''.join(reversed(wynik1))
reversed2 = ''.join(reversed(wynik2))
print(reversed1)
print(reversed2)

file1=open("wynik.txt", "a")
file1.write(reversed1 + "\n" + reversed2)
