with open('dataset_4.txt', 'r') as file_in, open('outtext.txt', 'w') as file_out:
    cnt = 0
    total_math = 0
    total_physics = 0
    total_language = 0
    for line in file_in:
        stroka = [str(i) for i in line.split(';')]
        math = int(stroka[1])
        total_math += math
        physics = int(stroka[2])
        total_physics += physics
        language = int(stroka[3])
        total_language += language
        averge_person = (math + physics + language) / 3
        file_out.write(str(averge_person))
        file_out.write('\n')
        cnt += 1
    averge_math = str(total_math / cnt)
    averge_physics = str(total_physics / cnt)
    averge_language = str(total_language / cnt)
    print(averge_math, averge_physics, averge_language, file=file_out)