def results(gamestotal):
    teamsresults = {}
    for i in range(gamestotal):                                 #считваем колво игр и результаты команд
        team1,score1,team2,score2 = input().split(';')          #вводим команды и их результат
        if team1 not in teamsresults:                          #проверяем наличие команды 1 в словаре
            teamsresults[team1] = [1, 0, 0, 0, 0]
        elif team1 in teamsresults:                            #если уже есть в словаре, прибавляем кол-во игр
            teamsresults[team1][0] += 1
        if team2 not in teamsresults:                          #проверяем наличие команды 2 в словаре
            teamsresults[team2] = [1, 0, 0, 0, 0]
        elif team2 in teamsresults:
            teamsresults[team2][0] += 1                        #прибавляем кол-во игр
        score1 = int(score1)                                    #преобразуем счёт в числа
        score2 = int(score2)
        if score1 > score2:                                     #если победа команды1
            teamsresults[team1][1] += 1                        # +1 победа
            teamsresults[team1][4] += 3                        # +3 очка за победу
            teamsresults[team2][3] += 1                        # +1 поражение команды2
        if score1 == score2:
            teamsresults[team1][2] += 1                        # +1 ничья команды1
            teamsresults[team2][2] += 1                        # +1 ничья команды2
            teamsresults[team1][4] += 1                        # +1 очко
            teamsresults[team2][4] += 1                        # +1 очко
        if score1 < score2:
            teamsresults[team1][3] += 1                        # +1 поражение команды1
            teamsresults[team2][1] += 1                        # +1 победа команды2
            teamsresults[team2][4] += 3                        # +3 очка команды2
    return teamsresults

def print_result(teamsresults):
    for key, value in teamsresults.items():                    # выводим результат
        print((key+':'), *value, end='\n')


def main():
    gamestotal = int(input())
    teamresults = results(gamestotal)
    print_result(teamresults)


if __name__ == '__main__':
    main()