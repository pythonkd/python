import re
def name_of_email(addr):
    b = re.compile(r'^([a-z]+)@.*$')
    s = b.match(addr)
    if s:
        return s.groups()[0]
    a = re.compile(r'^<?([a-zA-Z\s]+)>?\s.+$')
    s = a.match(addr).groups()
    return s[0]

if __name__ == '__main__':
    assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
    assert name_of_email('tom@voyager.org') == 'tom'
    print('ok')