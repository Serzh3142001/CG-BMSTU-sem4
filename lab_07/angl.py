with open('angl.txt') as f:
    lines = f.readlines()
    trueLines = []
    for line in lines:
        line = line.strip('\n')
        if ',' in line.split('-')[0]:
            for word in line.split('-')[0].split(', '):
                trueLines.append(f'{word} - {line.split("-")[1]}'.lower())
        else:
            trueLines.append(line.lower())

print(len(trueLines))
print(trueLines)

with open('angl2.txt', 'w') as f:
    for line in sorted(trueLines):
        f.write(line+'\n')