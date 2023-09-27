from sys import stdin

name2money = dict()
for line in stdin:
    operation = line.split()
    if operation[0] == "DEPOSIT":
        name, sum = operation[1:]
        name2money[name] = name2money.get(name, 0) + int(sum)
    elif operation[0] == "WITHDRAW":
        name, sum = operation[1:]
        name2money[name] = name2money.get(name, 0) - int(sum)
    elif operation[0] == "BALANCE":
        name = operation[1]
        if name in name2money:
            print(name2money[name])
        else:
            print("ERROR")
    elif operation[0] == "TRANSFER":
        name1, name2, sum = operation[1:]
        name2money[name1] = name2money.get(name1, 0) - int(sum)
        name2money[name2] = name2money.get(name2, 0) + int(sum)
    elif operation[0] == "INCOME":
        p = int(operation[1])
        for name in name2money:
            if name2money[name] > 0:
                name2money[name] = (name2money[name] * (100 + p)) // 100
    else:
        print("WRONG OPERATION")
