import glob


def file_parse():
    file_list = []
    for file in glob.glob("*.txt"):
        if file != 'res.txt':  # Excluding this file from the file_list
            file_list.append(file)
    result = []
    for file_name in file_list:
        with open(file_name, encoding='utf-8') as f:
            lines = f.readlines()
            lines_count = len(lines)
            result.append([file_name, lines_count, ''.join(lines)])
            # Sorting by second element (num of lines) of list
            result.sort(key=lambda x: x[1])
    # Writing lines to file
    with open('res.txt', 'w', encoding='utf-8') as f:
        for i in result:
            f.write(i[0] + '\n')
            f.write(str(i[1]) + '\n')
            f.write(i[2] + '\n\n')
    return result


res = file_parse()
