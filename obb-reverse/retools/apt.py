import os
dir = os.path.dirname(__file__)

with open(os.path.join(dir, '../files/history.log')) as file:
    for line in file:
        if 'Install: ' in line:
            print(line[9:], end='')