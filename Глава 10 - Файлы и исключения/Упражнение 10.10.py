filename = 'alice.txt'

with open(filename) as f:
    contents = f.read()
    print(contents.count('the'))
    print(contents.lower().count('the'))
    print()
    print(contents.count('the '))
    print(contents.lower().count('the '))
