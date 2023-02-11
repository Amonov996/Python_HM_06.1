with open('domen.txt') as f:
    domen = []
    for i in f.read().split('\n'):
        s = i.split('.')
        if f'.{s[-1]}' not in domen:
            domen.append(f'.{s[-1]}')
print(domen)