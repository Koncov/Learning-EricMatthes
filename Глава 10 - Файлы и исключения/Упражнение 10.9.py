# namefiles = ['cats.txt', 'dogs.txt']
namefiles = ['cats.txt', '_dogs.txt']

for namefile in namefiles:
    try:
        with open(namefile) as f:
            for line in f:
                print(line.rstrip())
    except FileNotFoundError:
        pass
        # print(f"Файл {namefile} отсутствует!")
