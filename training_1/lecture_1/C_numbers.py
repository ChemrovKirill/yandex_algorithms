def read_number():
    number = input()
    for s in '-+()':
        number = number.replace(s, '')
    if len(number) == 11:
        number = number[1:]
    elif len(number) == 7:
        number = '495' + number
    else:
        print('wrong number format')
        number = None
    return number

new_number = read_number()
for _ in range(3):
    book_number = read_number()
    if book_number == new_number:
        print('YES')
    else:
        print('NO')
