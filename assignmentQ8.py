A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
#The final value of A0 will be:
A0 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

A1 = range(10)
#The final value of A1 will be:
A1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

A2 = sorted([i for i in A1 if i in A0])
#The final value of A2 will be:
A2 = [1, 2, 3, 4, 5]

A3 = sorted([A0[s] for s in A0])
#The final value of A3 will be:
A3 = [1, 2, 3, 4, 5]

A4 = [i for i in A1 if i in A3]
#The final value of A4 will be:
A4 = [1, 2, 3, 4, 5]

A5 = {i: i*i for i in A1}
#The final value of A5 will be:
A5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

A6 = [[i, i*i] for i in A1]
#The final value of A6 will be:
A6 = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

A7 = reduce(lambda x, y: x+y, [10, 23, -45, 33])
#The final value of A7 will be:
A7 = 21

A8 = map(lambda x: x*2, [1, 2, 3, 4])
#The final value of A8 will be:
A8 = [2, 4, 6, 8]

A9 = filter(lambda x: len(x) > 3, ["I", "want", "to", "learn", "python"])
#The final value of A9 will be:
A9 = ['want', 'learn', 'python']

