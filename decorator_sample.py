# 関数内関数
def outer(func):
  def inner():
    print('---開始---')
    func()
    print('---終了---')
  return inner

@outer
def a():
  print('Aです')

a()

print('aaaaa\nbbb')
print('''テスト
ああああああ
あああああ
      テスト''')
# print(15 + '42')

num1 = 10
num2 = num1
print(id(num2))
num2 += 2
print(id(num2))
print(id(num1))


str = 'aaa'
srt2 = str

str2 = 'bbb'


str.upper
print(str)