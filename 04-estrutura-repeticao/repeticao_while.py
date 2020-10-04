'''
while
'''
pergunta = input('Bora da uma volta???[s/n] ')
n = 1
while pergunta != 's':
    pergunta = input(f'Bora{"a" * n} [s/n]? ')
    n+=1
    if 'chega' in pergunta:
        print("De boas!")
        break
else:
    print(f'Bora{"a" * n}, Partiu!')