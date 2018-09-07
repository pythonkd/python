def count_words(text: str, words: set) -> int:
    t=text.lower()
    s=t.split()
    sum={}
    for i in words:
        for j in s:
            if i in j:
                if i not in sum:
                    sum[i]=1
                else:
                    sum[i]+=1
    count=0
    for i in sum:
        count+=1
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")