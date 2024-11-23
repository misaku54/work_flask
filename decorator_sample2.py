# 関数
def outer(func):
  def inner(*args, **kwargs):
    print('---開始---')
    func(*args, **kwargs)
    print('---終了---')
  return inner

nums = (10, 20, 30, 40)

@outer
def show_sum(nums, **kwargs):
  sum = 0
  for num in nums:
    sum += num
    print(sum)


users = {'山田': 30, '田中': 40, '中村': 50}
@outer
def show_info(users):  
  for name, age in users.items():
    print(f'名前:{name}, 年齢:{age}')

show_sum(nums)
show_info(users)