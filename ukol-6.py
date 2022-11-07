r = {'1':'A', '2':'B', '3':'C', '4':'D', '5':'F'}

lines = []
with open('znamky.txt') as infile:
    for line in infile:
        for src, target in r.items():
            line = line.replace(src, target)
        lines.append(line)
with open('znamky.txt', 'w') as outfile:
    for line in lines:
        outfile.write(line)