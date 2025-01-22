def safe_division(a,b):
  try:
    return a/b
  except ZeroDivisionError:
      print("div zero impossible")
  