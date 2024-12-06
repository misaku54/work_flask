# 挿入ソート
def insertion_sort(array):
  print('初期値:',array)
  print('ーーーーーーーーーーー挿入ソートstartーーーーーーーーーーー')
  # 左端を操作済み→操作していない要素中で左端を取り出し→左の操作済みと比較
  # 左の数値が大きい場合、入れ替え。違う場合は左に左隣と比較し、自分より小さい数値が出るか一番左端にループがいくまで繰り返す。

  for i in range(1, len(array)):
    # ループに入る前に比較元を保存
    key_index = i

    for j in reversed(range(0, i)):
      print("i:",i)
      print("j:",j)
      print(array)
      # 隣接する左の要素の数値が大きい場合→入れ替えして次のループへ
      print(f'array[j]: {array[j]} > array[key_index]: {array[key_index]}')
      if array[j] > array[key_index]:
        tmp = array[j]
        array[j] = array[key_index]
        array[key_index] = tmp
        # 入れ替え後の比較元のキーを保存
        key_index = j
        continue
      # 隣接する左の要素の数値が小さい場合は比較のループを抜ける
      break

  print('ーーーーーーーーーーー選択ソートendーーーーーーーーーーーー')
  print('終了値:', array)


array = [9,1,7,4,5,6,2,3,8,10,12]
insertion_sort(array)