#task1---------------------------------------------
"""
Дан список чисел. Определите, сколько в нем встречается различных чисел.
"""
print(len(set(input().split())))
#-------------------------------------------------
#task2---------------------------------------------
"""
Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
"""
print(len((set(input().split())).intersection((set(input().split())))))
#-------------------------------------------------
#task3---------------------------------------------
"""
Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.
"""
c = ((list(((set(input().split())).intersection((set(input().split())))))))
t = []
for i in c:
    t.append(int(i))
t.sort()
print(' '.join([str(i) for i in t]))

#-------------------------------------------------
#task4---------------------------------------------
"""
Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
"""
numbers = [int(s) for s in input().split()]
occur_before = set()
for num in numbers:
    if num in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(num)

#-------------------------------------------------
#task5---------------------------------------------
"""
Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор и в каждом наборе все кубики различны по цвету. Однажды дети заинтересовались, сколько существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах. Для этого они занумеровали все цвета случайными числами от 0 до 108. На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части.

В первой строке входных данных записаны числа N и M — число кубиков у Ани и Бори. В следующих N строках заданы номера цветов кубиков Ани. В последних M строках номера цветов Бори.

Найдите три множества: номера цветов кубиков, которые есть в обоих наборах; номера цветов кубиков, которые есть только у Ани и номера цветов кубиков, которые есть только у Бори. Для каждого из множеств выведите сначала количество элементов в нем, а затем сами элементы, отсортированные по возрастанию.


"""
N, M = [int(i) for i in input().split()]
ncA = set([int(input()) for i in range(N)])
ncB = set([int(input()) for i in range(M)])
ncAB = ncA & ncB
ncA_only = ncA - ncB
ncB_only = ncB - ncA
print(len(ncAB))
print(*sorted(ncAB, key=int))
print(len(ncA_only))
print(*sorted(ncA_only, key=int))
print(len(ncB_only))
print(*sorted(ncB_only, key=int))
#-------------------------------------------------

#task6---------------------------------------------
"""
ан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько различных слов содержится в этом тексте.

Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
"""
n = int(input()) 
a = []
s = set()
for i in range(n):
    row = input().split()
    a.append(row)
for i in range(n):
    for j in range(len(a[i])):
        s.add(a[i][j])
print(len(list(s)))

#-------------------------------------------------

#task9------------------------------------------------------------
"""
Каждый из некоторого множества школьников некоторой школы знает некоторое количество языков. Нужно определить сколько языков знают все школьники, и сколько языков знает хотя бы один из школьников.

В первой строке задано количество школьников. Для каждого из школьников сперва записано количество языков, которое он знает, а затем - названия языков, по одному в строке.

В первой строке выведите количество языков, которые знаю все школьники. Начиная со второй строки - список таких языков. Затем - количество языков, 
которые знает хотя бы один школьник, на следующих строках - список таких языков. Языки нужно выводить в лексикографическом порядке, по одному на строке.
"""
def inpute(count):
    liste = set()
    for i in range(count):
        liste.add(input())
    return (liste)
liste = []
languages = set()
schools = set()
count_of_schools = int(input())
for j in range (count_of_schools):
    count_of_languages = int(input())
    liste.append(inpute(count_of_languages))
for j in range (count_of_schools-1):
    schools = schools | liste[j] & liste[j+1]
for j in range (count_of_schools-1):
    languages = languages | liste[j] | liste[j+1]
print (len(schools))
for i in range (len(schools)):
    print (list(schools)[i])
print (len(languages))
for i in range (len(languages)):
    print (list(languages)[i])
#----------------------------------------------------------------- 
