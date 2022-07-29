data = input("Введите пример: ")
v = 0
try:
  exec(f"v = {data}")
  print(f"Результат `{data}`:\n{v}")
except:
  print(f"Не удалось выполнить `{data}`")