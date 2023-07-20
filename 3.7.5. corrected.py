
# передать в функции r и w название файла


def read_file(file_in_name):
    with open(file_in_name, 'r') as file_in:
        student_count = {}
        class_total_height = {}
        for line in file_in:
            student = [str(i) for i in line.split()]
            student_class = int(student[0])
            student_height = int(student[2])
            if student_class in class_total_height:
                class_total_height[student_class] += student_height
                student_count[student_class] += 1
            if student_class not in class_total_height:
                class_total_height[student_class] = student_height
                student_count[student_class] = 1
        return student_count, class_total_height


def list_of_students(student_count, class_total_height):
    class_list_output = {1: '-', 2: '-', 3: '-', 4: '-', 5: '-', 6: '-', 7: '-', 8: '-', 9: '-', 10: '-',
                         11: '-'}
    for key in class_total_height:  # изменение значений в конечном словаре
        class_list_output[key] = class_total_height[key] / student_count[key]
    sorted_list = sorted(class_list_output.items())
    return sorted_list


def write_file(file_out_name, sorted_list):
    with open(file_out_name, 'w') as file_out:
        for key, value in sorted_list:
                string = str(key) + ' ' + str(value)
                file_out.write(string)
                file_out.write('\n')



def main():
    student_count, class_list = read_file('dataset_1.txt')
    final_result = list_of_students(student_count, class_list)
    write_file('output.txt', final_result)



if __name__ == '__main__':
    main()



