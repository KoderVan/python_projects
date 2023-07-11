def main():
    pass


if __name__ == '__main__':
    main()
    with open('dataset_1.txt', 'r') as file_in, open('output.txt', 'w') as file_out:
        student_count = {}                                       #счётсчик учеников каждого класса класса
        class_list = {}                                          #счётчик суммарного роста учеников каждого класса
        class_list_output = {1: '-', 2: '-', 3: '-', 4: '-', 5: '-', 6: '-', 7: '-', 8: '-', 9: '-', 10: '-', 11: '-'}
        for line in file_in:
            student = [str(i) for i in line.split()]
            student_class = int(student[0])
            student_height = int(student[2])
            if student_class in class_list:
                class_list[student_class] += student_height
                student_count[student_class] += 1
            if student_class not in class_list:
                class_list[student_class] = student_height
                student_count[student_class] = 1
        for key in class_list:                           #изменение значений в конечном словаре
            class_list_output[key] = class_list[key] / student_count[key]
        sorted_list = sorted(class_list_output.items())
        for key, value in sorted_list:
            string = str(key) + ' ' + str(value)
            file_out.write(string)
            file_out.write('\n')
            string = ''
