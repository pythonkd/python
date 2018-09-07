def sun_angle(time):
    s=time.split(":")
    a=int(s[0])*60+int(s[1])
    if a>(18*60) or a<(6*60):
        return "I don't see the sun!"
    else:
        angle=(a-6*60)*0.25
        return angle

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")