from pathlib import Path

d = {}

with open("en-ru.txt","r") as file:
    for line in file:
        en_ru = line.split("-")[0].strip()
        ru_en = line.split("-")[1].strip().split(',')
        for i in ru_en:
            i = i.strip()
            if i in d.keys():
                d[i] = d[i] + ", " + en_ru
            else:
                d[i] = en_ru

with open("ru-en.txt", "w") as file:
    for i in sorted(d.keys()):
        file.writelines(f"{i} - {d[i]}\n")


with open('ru-en.txt', 'rt') as file:
    content = file.read()
    items = content.split(':')
    b = items.sort(content)
    content = ','.join(items)
with open('ru-en.txt', 'wt') as dst:
    dst.write(content)


