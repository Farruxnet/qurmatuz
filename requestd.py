def filter_number(txt):
    number = ''
    for s in txt:
        if s.isdigit():
            number += s
    if len(number) == 12:
        number = '+'+number
    elif len(number) == 9:
        number = '+998'+number
    elif len(number) == 10:
        number = '+99'+number
    else:
        number = number
    return number


print(filter_number("90-940 499 7"))
