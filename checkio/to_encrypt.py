def to_encrypt(text, delta):
    s=''
    for i in text:
        if ord(i)== 32:
            s+= chr(32)
        elif ord(i) + delta > 122:
            s = s + chr(ord('a')+ord(i)+delta-ord('z')-1)
        elif ord(i) + delta < 97:
            s = s + chr(ord('z')-ord('a')+ord(i)+delta +1 )
        else:
            s = s +chr(ord(i)+delta)
    return s
if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")