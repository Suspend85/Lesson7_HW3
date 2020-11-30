def file_parse():
    result = []
    num_of_files = 3  # Set number of file we need to parse

    for i in range(1, num_of_files+1):  # generate name of file to read him
        filename = '{0}.txt'.format(i)
        with open(filename, encoding='utf-8') as f:
            lines = f.readlines()
            lines_count = len(lines)
            result.append([filename, lines_count, ''.join(lines)])
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
