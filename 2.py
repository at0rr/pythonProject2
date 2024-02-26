import csv


def sort_d(data: list):
    for i in range(1, len(data)):
        nom = data[i]
        age = nom['date']
        j = i - 1
        while j >= 0 and data[j]['date'] > age:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = nom

with open('songs.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    data = list(reader)
    sort_d(data)
file.close()
with open('songs_new.csv', 'w', newline='', encoding='utf-8') as file:
    f = ['№', 'Название песни', 'Артист', 'Дата выхода']
    writer = csv.DictWriter(file, fieldnames=f, delimiter=';')
    writer.writeheader()
    writer.writerows(data)
