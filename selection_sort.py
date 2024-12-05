# 選択ソート
# 線形探索で最小値を検索し、その最小値を右恥に設置してソート完了
# 次の要素から線形探索→最小値の検索を行う。

# 対象
# array = [9,8,7,6,5,4,3,2,1,]
array = [9,1,7,4,5,6,2,3,8,]

def selection_sort(array):
  print('初期値:',array)
  print('ーーーーーーーーーーー選択ソートstartーーーーーーーーーーー')

  for i in range(0, len(array)):
    # 最小値のインデックス
    # print(i)
    min_idx = i
    tmp = min_idx

    for j in range(i + 1, len(array)):
      # 比較  
      if array[min_idx] > array[j]:
        min_idx = j

    # 最小値が変わらなかったら次のループへ
    if min_idx == i:
      continue
    # 最小値を左端に格納し、入れ替える
    tmp = array[i]
    array[i] = array[min_idx]
    array[min_idx] = tmp
    print(array)

  print('ーーーーーーーーーーー選択ソートendーーーーーーーーーーーー')
  print('終了値:', array)

selection_sort(array)