file_name = 'alice.txt'

try:
    with open(file_name, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry? the file {file_name} does not exist.")
else:
    # Подсчет приблизительное количества слов в тексте.
    words = contents.split()
    num_words = len(words)
    print(f"The file {file_name} nas about {num_words} words.")
    # print(worlds)
    # print(num_worlds)
