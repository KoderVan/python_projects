with open('dataset_3363_3.txt', 'r') as file_in, open('outtext.txt', 'w') as file_out:
    new_list = {}
    out_list = {}
    string = ''
    sorted_list = []
    for line in file_in:
        for i in line.split():
            if i not in new_list:
                new_list[i] = 1
            elif i in new_list:
                new_list[i] += 1
    spisok = list(new_list.values())
    a = max(spisok)

    for key, value in new_list.items():
        if value == a:
            out_list[key] = value

    out_list_sort = sorted(out_list.items())
    for key, value in out_list_sort:
        string = str(key) + ' ' + str(value)
        file_out.write(string)
        file_out.write('\n')
        string = ''









