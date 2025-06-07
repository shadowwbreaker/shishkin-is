import sys


def process_poem():
    try:
        encodings = ['utf-8', 'utf-16', 'cp1251', 'iso-8859-1']

        for encoding in encodings:
            try:
                with open('text18-29.txt', 'r', encoding=encoding) as f:
                    lines = f.readlines()
                    content = ''.join(lines)
                break
            except UnicodeDecodeError:
                continue
        else:
            raise ValueError("Не удалось определить кодировку файла")

        print(content)
        print(len(content))

        if len(lines) >= 4:
            lines.insert(2, lines.pop())

        with open('poem_modified.txt', 'w', encoding='utf-8') as f:
            f.writelines(lines)

    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    process_poem()