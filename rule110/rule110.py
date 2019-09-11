seed = [1,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1]
rows = len(seed)

# Rule 110
rules = [[1,1,0],[1,0,1],[0,1,1],[0,1,0],[0,0,1]]

prev_line = seed
new_line = [0]

for i in range(1, rows-1):
    scan = [prev_line[i-1], prev_line[i], prev_line[i+1]]
    if scan in rules:
        new_line += [1]
    else:
        new_line += [0]

new_line += [0]

print(seed)
print(new_line)


