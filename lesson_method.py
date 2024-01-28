s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
#Myから始まっているかどうかを尋ねる関数
print(is_start)

print('#############')

print(s.find('Mike'))
#Mikeは何文字目から始まりますか
print(s.rfind('Mike'))
#後ろのMikeは何文字目から始まりますか
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))

#f-strings

a = 'a'
print(f'a is {a}')
x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')