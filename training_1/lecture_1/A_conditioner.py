troom, tcond = map(int, input().split())
mode = input()
if mode == "fan":
    print(troom)
elif mode == "auto":
    print(tcond)
elif mode == "freeze":
    if troom > tcond:
        print(tcond)
    else:
        print(troom)
elif mode == "heat":
    if troom < tcond:
        print(tcond)
    else:
        print(troom)
        