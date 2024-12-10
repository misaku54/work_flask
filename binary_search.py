# 前提として既に整列されていること
# 探索する数値がある
# 配列の中心の数を調べる
# 探索数値と中心の数を比較する
# 探索数値が大きければ、中心の数より右側になることがわかる
# 中心の数以下以上の数値を候補から除外する
# 残った数の中心値を調べる（４つの場合は二つ目を中心値とする）
# 探索数値と中心の数を比較する
# 中心の数以下以上の数値を候補から除外する
# 中心の数を調べる
# 中心の数＝検索値ならその番号を表示して終了


def binary_search(array, value):
  # 左端
  left = 0
  # 右端
  right = len(array) - 1

  # ループ
  while left <= right:
    # 中心値を求める(商を求める)
    mdl_idx = (left + right) // 2

    if value > array[mdl_idx]:
      left = mdl_idx + 1
    elif value < array[mdl_idx]:
      right = mdl_idx - 1
    else:
      # イコール
      return mdl_idx
  
  # 検索値が見つからない場合
  return None
  
value = 17
array = [2,3,5,6,17,19,100]
youso = binary_search(array, value)
if youso is not None:
  print(f'value:{value}は、arrayの{youso + 1}番目にあります')
else:
  print('見つかりませんでした')