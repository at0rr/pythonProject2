import csv

with open('songs.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter=';'))[1:]
with open('songs_new.csv', 'w', encoding='utf8', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['streams', 'artist_name', 'track_name', 'date'])
    writer.writerows(reader)

sum_class = {}
col_class = {}
for streams, artist_name, track_name, date in reader:
    if
