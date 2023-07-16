def main():
    pass


if __name__ == '__main__':
    main()
    directions_count = int(input())

    def movement():
        latitude = 0
        longitude = 0
        direction_list = []
        for i in range(directions_count):
            direction = input().split(' ')
            direction[1] = int(direction[1])
            if direction[0] == 'восток':
                latitude += direction[1]
            if direction[0] == 'запад':
                latitude -= direction[1]
            if direction[0] == 'север':
                longitude += direction[1]
            if direction[0] == 'юг':
                longitude -= direction[1]
        print(latitude,longitude)

movement()


