# %%

#  exemplo de somatorio

#  somatorio de 1 a 10 de i
total = 0
for i in range(1, 11):
    total += i
print(total)

# %%

# somatorio de 1 a 3 de i^2
total = 0
for i in range(1, 4):
    total += i**2
print(total)

# %%

# somatorio de 10 a 30 de i²

total = 0
for i in range(10, 31):
    total += i**2
print(total)

# %%

# somatoria de 1 a 3 de i²-1

total = 0
for i in range(1, 4):
    total += (i**2) - i
print(total)

# %%

# somatória de um vetor
x = [45, 60, 42, 50, 55, 47]

total = 0
for i in range(len(x)):
    total += x[i]
print(total)

# %%

# somatória do vetor com divisão para achar a média

total = 0
for i in range(len(x)):
    total += x[i] / 6
print(total)

# %%

# outra forma de achar a média, as duas são válidas
x = [45, 60, 42, 50, 55, 47]

total = 0
for i in range(len(x)):
    total += x[i]

media = total / len(x)
print(media)
