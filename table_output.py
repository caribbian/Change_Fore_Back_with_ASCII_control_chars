
# from sys import stdout
# #from tabulate import tabulate
# stdout_fileout=stdout 
# out=[
#       ['А.С Пушкин', 'Капитанская дочка', '1836\n'], 
#       ['М.Ю Лермонтов', 'Бородино', '1837\n'], 
#       ['И.С Тургенев', 'Муму', '1852']
#       ]
# for i in out:
#     stdout_fileout.write("{: <20} {: <20} {: >20}".format(*i))

# #########################################################################################################################

# from sys import stdout

# list1 = ['А.С Пушкин', 'М.Ю Лермонтов', 'И.С Тургенев']
# list2 = ['Капитанская дочка', 'Бородино', 'Муму']
# list3 = ['1836', '1837', '1852']

# l = []

# for i in range(0, len(list1)):
#     l.append(list1[i]), l.append(list2[i]), l.append(list3[i])

# #print(l)

# for i in range(0, len(l), 3):
#     print("{: <20}".format(l[i]), "", "{: <20}".format(l[i + 1]), "", "{: >10}".format(l[i+2]))

###########################################################################################################################

from sys import stdout
stdout.write('А.С Пушкин              Капитанская дочка 1836\n')
stdout.write('М.Ю Лермонтов                    Бородино 1837\n')
stdout.write('И.С Тургенев                         Муму 1852')