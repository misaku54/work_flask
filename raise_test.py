

# （正常パターン）文字の数値をfloat型に明示的にキャストしてaに代入
a = float("1")
print(a)

# ValueErrorとは、引数の型はあっているけれど誤った値を取っている場合に発生する例外です。
# （例外パターン）文字をfloat型に明示的にキャストしようとするが、引数の型(str)は合っているが誤った値のため変換できずValueError
b = float("abc")
print(b)