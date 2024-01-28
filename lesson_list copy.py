i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =', i)
print('i =', i)


x = [1, 2, 3, 4, 5]
y = x.copy()
#y = x[:でも同じ。ただし見やすいように上記method推奨
y[0] = 100
print('y =', x)
#整数や数字は値渡し、リスト、ディクショナリーは参照渡し
X = 20
Y = XY = 5
print(id(X))
print(id(Y))
#idが違うように、XとYは違うもの
print(Y)
print(X)

X = ['q', 'b']
Y = X
Y[0] = 'p'
print(id(X))
print(id(Y))
print(Y)
print(X)
