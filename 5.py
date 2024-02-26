import csv


def g_hash(s: str):
    alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    d = {n: i for i, n in enumerate(alph, 1)}
    p = 67
    m = 10 ** 9 + 9
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + d[c] * p_pow) % m
        p_pow = (p_pow * p) % m
    return int(hash_value)


hash = []
with open('songs.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter=';'))[1:]
    for row in reader:
        row[0] = g_hash(row[1])
        hash.append(row)
with open('songs.csv', 'w', newline='', encoding='utf8') as file:
    w = csv.writer(file)
    w.writerow('streams;artist_name;track_name;date')
    w.writerows(hash)