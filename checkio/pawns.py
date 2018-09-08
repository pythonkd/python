def safe_pawns(pawns: set) -> int:
    t=[]
    s=filter(judge,pawns)
    for i in s:
        if chr(ord(i[0])+1)+str(int(i[1])-1)  in pawns:
            t.append(i)
        elif chr(ord(i[0])-1)+str(int(i[1])-1) in pawns:
            t.append(i)
    return len(t)
def judge(n):
    if int(n[1]) == 1:
        return False
    return True
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")