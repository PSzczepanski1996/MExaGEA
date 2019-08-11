import os
dir = os.path.dirname(__file__)

with open(os.path.join(dir, '../files/dpkg.log')) as file:
    for line in file:
        if 'installed' in line:
            print(line[27:], end='')