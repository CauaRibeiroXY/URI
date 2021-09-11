while True:
  try:
    h,v = input().split(' ')
    
    print(abs(int(h)-int(v)))
  except EOFError:
    break
