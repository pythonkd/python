from collections import  Counter
def checkio(text: str) -> str:
    a = list(filter(nonum, text))
    b = []
    for i in a:
        b.append(i.lower())
    x = sorted(Counter(b).most_common(), key=lambda x: x[1], reverse=True)

    def p(n):
        if n[1] < x[0][1]:
            return False
        else:
            return True

    return sorted(list(filter(p, x)), key=lambda x: x[0])[0][0]


def nonum(n):
    if n.isdigit():
        return False
    if ord(n) < 65 or 90 < ord(n) < 97 or ord(n) > 122:
        return False
    else:
        return True


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")