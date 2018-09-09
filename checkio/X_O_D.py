from typing import List


def checkio(game_result: List[str]) -> str:
    g = game_result
    s = ['', '', '', ]
    l = ['', '']
    for i in range(3):
        for j in g:
            s[i] += j[i]
    j = 0
    k = 2
    for i in g:
        l[0] += i[j]
        l[1] += i[k]
        j += 1
        k += -1
    total = s + l + g

    if "XXX" in total:
        return "X"
    if 'OOO' in total:
        return "O"
    return "D"

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")