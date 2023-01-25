
def open_file(file_name):
    keyword_list = []
    real_books = []
    x = 0

    with open(file_name) as books_txt:
        old_books = list(books_txt.readlines())

    for line in old_books:
        if not line.isspace():
            line = line.strip()
            real_books.append(line)

    for line in real_books:
        x += 1
        line = line.lower()
        if 'keyword' in line:
            keyword_list.append(real_books[x])

    for line in keyword_list:
        print(line.lower())
    # print(keyword_list)

open_file('blurbary_books_new.txt')


