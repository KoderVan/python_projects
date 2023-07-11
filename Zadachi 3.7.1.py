gamestotal = int(input())
teamsresoults = {}
for i in range(gamestotal):                                 #считваем колво игр и результаты команд
    team1,score1,team2,score2 = input().split(';')          #вводим команды и их результат
    if team1 not in teamsresoults:                          #проверяем наличие команды 1 в словаре
        teamsresoults[team1] = [1, 0, 0, 0, 0]
    elif team1 in teamsresoults:                            #если уже есть в словаре, прибавляем кол-во игр
        teamsresoults[team1][0] += 1
    if team2 not in teamsresoults:                          #проверяем наличие команды 2 в словаре
        teamsresoults[team2] = [1, 0, 0, 0, 0]
    elif team2 in teamsresoults:
        teamsresoults[team2][0] += 1                        #прибавляем кол-во игр
    score1 = int(score1)                                    #преобразуем счёт в числа
    score2 = int(score2)
    if score1 > score2:                                     #если победа команды1
        teamsresoults[team1][1] += 1                        # +1 победа
        teamsresoults[team1][4] += 3                        # +3 очка за победу
        teamsresoults[team2][3] += 1                        # +1 поражение команды2
    if score1 == score2:
        teamsresoults[team1][2] += 1                        # +1 ничья команды1
        teamsresoults[team2][2] += 1                        # +1 ничья команды2
        teamsresoults[team1][4] += 1                        # +1 очко
        teamsresoults[team2][4] += 1                        # +1 очко
    if score1 < score2:
        teamsresoults[team1][3] += 1                        # +1 поражение команды1
        teamsresoults[team2][1] += 1                        # +1 победа команды2
        teamsresoults[team2][4] += 3                        # +3 очка команды2
for key, value in teamsresoults.items():                    # выводим результат
    print((key+':'), *value, end='\n')