def process_file(filename):
    f = open(filename, 'r')
    sorted_items = []
    num_lines = 0
    for line in f:
        num_lines += 1
        clean_line = line.strip()
        clean_line = clean_line.lower()
        sorted_items += clean_line
        sorted_items.sort()
    number_of_lines = (num_lines)
    print filename, number_of_lines, sorted_items
    return filename, sorted_items, number_of_lines

process_file('./common_words_100.txt')
