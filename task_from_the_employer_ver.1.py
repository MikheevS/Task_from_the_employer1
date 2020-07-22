#Напишите, пожалуйста, программу на любом языке программирования, которая поместит + (2+3), - (3-2), или ничего ( ) в промежутках между цифрами от 9 до 0 (в таком порядке) так, чтобы в результате получилось 200. Например: 98+76-5+43-2-10=200.
from itertools import product
sum_num = 200
digits = '987654321'
signs = '', '+', '-'
parts = []
for i in digits:
    parts.append([i + signs[0],i + signs[1], i + signs[2]])

for index in product(range(3), repeat=9):
    expr = "".join([parts[i][index[i]] for i in range(9)])
    expr += '0'
    if eval(expr) == sum_num:
        print(expr + '=' + str(sum_num))