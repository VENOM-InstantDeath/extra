def calc(a, op, b):
    a = (a[0]*60)+a[1]
    b = (b[0]*60)+b[1]
    if op == '+':
        r = a + b
    if op == '-':
        r = a - b
    r = [r // 60, r % 60]
    return f"{r[0]}:{r[1]}"

if __name__ == "__main__":
    import re
    while True:
        x = input(':hcalc:> ')
        if x == "exit": exit(0)
        op = re.findall('[+-]', x)
        if len(op) > 1:
            print("Cuentas de más de una operación no están soportadas")
            continue
        x = re.split('[+-]', x)
        for i in range(len(x)): x[i] = x[i].split(':')
        for i in range(len(x)):
            x[i] = [int(i) for i in x[i]]
        a, b = (x[0], x[1])
        op = op[0]
        if len(a) != 2: a.insert(0, 0)
        if len(b) != 2: b.insert(0, 0)
        print(calc(a, op, b))

