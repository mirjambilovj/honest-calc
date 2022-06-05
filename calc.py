messages = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)"
    ]

operators = ["+", "-", "*", "/"]

memory = 0


def is_one_digit(v):
    if -10 < v < 10:
        return v.is_integer()
    return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += messages[6]
    if v1 == 1 or v2 == 1 and v3 == "*":
        msg += messages[7]
    if (v1 == 0 or v2 == 0) and (v3 in ["*", "+", "-"]):
        msg += messages[8]
    if msg != "":
        msg = messages[9] + msg
        print(msg)


while True:
    print(messages[0])

    calc = input()
    x, oper, y = calc.split()

    if x == "M":
        x = memory

    if y == "M":
        y = memory

    try:
        x = float(x)
        y = float(y)
    except:
        print(messages[1])
        continue

    if oper not in operators:
        print(messages[2])
        continue

    check(x, y, oper)

    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/" and y != 0:
        result = x / y
    else:
        print(messages[3])
        continue

    print(result)

    print(messages[4])
    answer = ""
    while answer == "":
        answer = input()
        if answer == 'y':
            if is_one_digit(result):
                answer = ""
                msg_index = 10

                while True:
                    print(messages[msg_index])
                    answer = input()
                    if answer == 'y' and msg_index < 12:
                        msg_index += 1
                        continue
                    elif answer == 'n':
                        break
                    else:
                        memory = result
                        break
            else:
                memory = result
        elif answer == 'n':
            pass
        else:
            continue

    print(messages[5])
    answer = ""
    while answer == "":
        answer = input()
        if answer not in ['y', 'n']:
            continue

    if answer == 'y':
        continue
    else:
        break