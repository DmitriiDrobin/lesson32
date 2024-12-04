def custom_write(file_name, strings):
    strings_positions = {}
    b = 0
    file = open(file_name, 'w', encoding='utf-8')
    for a in strings:
        c = file.tell()
        file.write(a + '\n')
        b += 1
        strings_positions[(b, c)] = a
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

