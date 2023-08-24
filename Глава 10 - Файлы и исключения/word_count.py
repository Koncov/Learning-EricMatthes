def count_words(filename):
    """Подсчет приблизительного количества слов в тексте"""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # pass
        print(f"WARNING!   --= The file {filename} does not exist. Sorry! =--")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} nas about {num_words} words.")


filenames = ['alice.txt', '_siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
