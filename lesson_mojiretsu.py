s = 'test'
print('hello')
print("hello")
print("I don't know")
print("I don\'t know")
print('say "I don\'t know"')
print("say \"I don't know\"")


print('hello.\nHow are you?')
#\n は改行を表す

print(r'C:\name\name')
#r = rawの意味

print("""
line1
line2
line3
""")
print("##############")
#間に改行が入ってしまう

print("""\
line1
line2
line3\
""")
print("##############")

print('Hi.' * 3 + 'Mike.')

print('Py' + 'thon')
print('Py' 'thon')
prefix = 'Py'
#print(prefix 'thon') このように一旦変数に入れたリテラルはエラーが出る
print(prefix + 'thon')

# + を使わない時何がいいのか

s = ('aaaaaaaaaaaaaaa' 'bbbbbbbbbbbbbbbb')
#文字列が長いとコードが見えなくなるため、改行して見やすくしたいときに使う
print(s)

a = ('aaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbb')
#a = 'aaaaaaaaaaaaaaa'\
#     'bbbbbbbbbbbbbbbb'  これも同じ意味。ただし()の方が好まれる
print(a)

word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:1])
print(word[0:2])
#スライス
print(word[2:5])
print('############')
print(word[0:2])
print(word[:2])
print('#############')
print(word[2:])
#print(word[100]) エラー出る
print('#############')
word = 'j' + word[1:]
#１文字置き換え word[0] = 'j' だとエラー
print(word)
print(word[:])
#word全てのコピーという意味になる
n = len(word)
#インデックスの長さ
print(n)