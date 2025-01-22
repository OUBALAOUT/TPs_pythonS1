def safe_division(a,b):
  try:
    v = a/b
  except ZeroDivisionError:
      print("div zero impossible")
  else:
      print("succes")
      return v
  finally:
      print("done")
      
print(safe_division(0,4))