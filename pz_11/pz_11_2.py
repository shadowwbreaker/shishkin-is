#2. Из предложенного текстового файла (text18-29.txt) вывести на экран его содержимое,
#количество символов в тексте. Сформировать новый файл, в который поместить текст в
#стихотворной форме предварительно поставив последнюю строку между второй и третьей
def read_file(filename):
    encodings = ['utf-8', 'utf-16', 'windows-1251']
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                return file.readlines()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Не удалось декодировать файл {filename} с помощью {encodings}")

lines = read_file('text18-29.txt')

print("Содержимое файла:")
for line in lines:
    print(line.strip())

char_count = sum(len(line.strip()) for line in lines)
print(f"\nКоличество символов в тексте: {char_count}")

if len(lines) >= 3:
    last_line = lines.pop()
    lines.insert(2, last_line)

with open('modified_text18-29.txt', 'w', encoding='utf-8') as file:
    file.writelines(lines)

print("\nИзмененный текст сохранен в файл 'modified_text18-29.txt'")
