def check_connection(network, first, second):
    t = []
    u = {first}
    for i in network:
        s = i.split('-')
        t.append(s)
  #  print(t)
    k = len(t)
 #   print(k)
    while k!=0:
        k -= 1
        s = []
        for i in u:
            for j in t:
                if i in j:
                    for n in j:
                        s.append(n)
        for i in s:
            u.add(i)
    if second in u:
        return True
    return False
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."