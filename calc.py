def calculate():
  print("簡易電卓アプリケーションです。終了するには '=' を入力してください。")
  try:
    result = float(input("数値を入力してください: "))
  

    while True:
      operation = input("操作を選択してください (+, -, *, /, =): ")
      white_op_list = ('+', '-', '*', '/')

      # =入力により結果を表示しループ終了
      if operation == '=':
        print(f"計算結果{result}")
        break
      elif operation in white_op_list:
        number = float(input("数値を入力してください: "))
        if operation == '+':
          result += number
        elif operation == '-':
          result -= number
        elif operation == '*':
          result *= number
        elif operation == '/':
          # 割る数値が０の場合はメッセージ出力し次のループへ
          if number != 0:
            result /= number
          else:
            print('0では割れない')
            continue
      else:
        print('無効な操作です')
  except ValueError as e:
    print(e)
    print('処理を終了します。')

# 実行
calculate()