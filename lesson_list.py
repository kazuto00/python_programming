l = [1, 20, 4, 50, 2, 1, 2]
print(l)

print(l[1])
print(l[0])
print(l[-1])
print(l[-2])
print(l[:2])
print(l[2:5])
print(l[2:])
print(l[:])
print(len(l))
print(type(l))
print(list('abcdefg'))
print('###########')
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
print(n[::2])
#一つ飛ばしで出力
print(n[::-1])

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
#ネスト
print(x[1])
print(x[0][1])
print(x[1][2])
print('##############')
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s[0])
s[0] = 'X'
print(s[0])
#文字列の入れ替えはエラー出るが、配列の場合は書き換え可能
s[2:5] = ['C', 'D', 'E']
print(s)
s[2:5] = []
print(s)
print(s[:])
s[:] = []
print(s)
print('##########')
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
n.append(100)
print(n)
n.insert(0, 200)
print(n)
n.pop()
print(n)
n.pop(0)
print(n)
del n[0]
print(n)
#del n としてしまうと、nの定義自体が消えてしまうため使い所注意
n.remove(2)
n = [1, 2, 2, 2, 3]
print(n)
n.remove(2)
print(n)
n.remove(2)
n.remove(2)
print(n)
print('#########')

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
x = a + b
print(x)
a += b
print(a)
print('########')

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
print(x)
print('######')

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
#リスト中の何番目にあるか
print(r.index(3, 3))
print(r.count(3))
#3が何個あるか
if 5 in r:
    print('exist')
print('#########')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)
print('#######')

s = 'My name is Mike'
to_split = s.split(' ')
#''の間の文字で分けてリスト化
print(to_split)

x = ' '.join(to_split)
#リストを''の間の文字で繋げてください
print(x)
x = '######'.join(to_split)
print(x)
print('########')

print(help(list))