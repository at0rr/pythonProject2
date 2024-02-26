import csv
with open('songs.csv', 'r', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=';')
    name = input()
    while name != '0':
        for streams, artist_name, track_name, date in reader:
            if name == artist_name:
                print(f'У {artist_name} найдена песня: {track_name}')
                break
        else:
            print('К сожалению, ничего не удалось найти')

        name = input()
