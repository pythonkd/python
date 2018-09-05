def checkio(data: str) -> bool:
    if len(data) < 10:
        return False
    if not data.isalnum():
        return False
    x = 0
    for i in data:
        if i.isdigit():
            x = 1
    y = 0
    for i in data:
        if 97 <= ord(i) <= 122:
            y = 1
    z = 0
    for i in data:
        if 65 <= ord(i) <= 90:
            z = 1
    if x == 1 and y == 1 and z == 1:
        return True
    else:
        return False


# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")