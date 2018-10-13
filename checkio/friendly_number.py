def friendly_number(number, base=1000, decimals=0, suffix='', powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    i = 0
    #print(number)
    if number > pow(1000, len(powers)):
        number /= pow(1000, len(powers) - 1)
        i = len(powers) - 1
    else:
        while abs(number) >= base:
            number = number / base
           # print(number)
            i = i + 1
            if i >= len(powers) - 1:
                i = len(powers) - 1
                break

    #print(number)
    # 找出合适的number
    number = float(number)
    if decimals == 0:
        number = str(int(number))
    else:
        s = str(number).split(".")
        # 判断档后几位数全是零
        if int(s[1]) == 0:
            number = s[0] + "." + "0" * decimals
        else:
            a = s[1][:decimals + 1]
            if int(a[-1]) >= 5:
                a = str(int(a[:decimals]) + 1)
            else:
                a = a[:decimals]
            # print(a)
            number = s[0] + "." + a

    return number + powers[i] + suffix
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'