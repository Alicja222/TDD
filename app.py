from funkcjafizz import *

x = int(input('Do ilu gramy w fizzbuzz? '))
for i in range(1, x+1):
    print(i, ' --> ', fizzbuzz(i))