import re


def process_hotlines():
    with open('hotline1.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    phone_pattern = re.compile(r'8\(\d{3}\)\d{3}-\d{2}-\d{2}')
    phones = phone_pattern.findall(content)

    modified_content = re.sub(
        r'(«Горячая линия»)(?! Министерства)',
        r'\1 Министерства образования Ростовской области',
        content
    )

    with open('hotline_processed.txt', 'w', encoding='utf-8') as new_file:
        new_file.write(modified_content)

    print(len(phones))
    for phone in phones:
        print(phone)


if __name__ == "__main__":
    process_hotlines()