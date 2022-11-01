with open('znamky.txt', 'r', encoding='utf-8') as file:
    znamky = file.readlines()

with open('file.txt', 'r') as file :
  filedata = file.read()

znamky = znamky.replace('1', 'A')

with open('file.txt', 'w') as file:
  file.write(znamky)