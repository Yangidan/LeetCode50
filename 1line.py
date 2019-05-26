""" Fractal """
# print('\n'.join([''.join(['*'if abs((lambda a: lambda z, c, n: a(a, z, c, n))(lambda s, z, c, n: z if n == 0 else s(s, z*z+c, c, n-1))(0, 0.02*x+0.05j*y, 40)) < 2 else ' ' for x in range(-80, 20)]) for y in range(-20, 20)]))

""" Heart """
# print('\n'.join([''.join([('DanLove'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

""" Archimedean spiral """
# exec("""\nfrom turtle import *\nfor i in range(500): \n    forward(i)\n    left(91)\n""")

""" quick sort """
# quickSort = lambda array: array if len(array) <= 1 \
# else quickSort([item for item in array[1:] \
# if item <= array[0]]) + [array[0]] + quickSort([item for item in array[1:] if item > array[0]])
# array = [9, 11, 88, 32, 8]
# print(quickSort(array))

""" cmd line """
# python -c "while 1:import random;print(random.choice('|| __'), end='')"

ab = [[1, 2, 3], [5, 8], [7, 8, 9]]
# print([i for i in item for item in ab])  """ NameError: name 'item' is not defined """
print([i for item in ab for i in item])

