try:
  target = save = int(input('Please enter number! > '))
  while not save == 1:
    if save % 2 == 1:
      save = save * 3 + 1
    else:
      save = save // 2
    print(save)
  print(f'target:{target} clear!')
except:
  print('It\'s not number!')
