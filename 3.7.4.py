





def movement(directions_count):
    latitude = 0
    longitude = 0
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
    return latitude, longitude


def main():
    latitude_end, longitude_end = movement(int(input()))
    print(latitude_end, longitude_end)

if __name__ == '__main__':
    main()