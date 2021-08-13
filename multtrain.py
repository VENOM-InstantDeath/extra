import random
import re

def main():
    while True:
        intervalo = input("Intervalo: ")
        if not re.match('^[0-9]+:[0-9]+$', intervalo):
            print("\033[1;31mFormato de intervalo incorrecto\033[0m")
            continue
        else:
            break
    #10+10 = 20
    l = (len(intervalo.split(':')[1])*3)+15
    c = 0
    intervalo = [int(i) for i in intervalo.split(':')]
    for i in range(10):
        a = random.randint(*intervalo)
        b = random.randint(*intervalo)
        print(f"{a}*{b} = ", end='')
        resp = input()
        if not resp.isdigit():
            print(f"\033[1A\033[{l}C\033[1;31mIncorrecto\033[0m")
            continue
        if int(resp) == a*b:
            print(f"\033[1A\033[{l}C\033[1;32mCorrecto\033[0m")
            c += 1
            continue
        else:
            print(f"\033[1A\033[{l}C\033[1;31mIncorrecto\033[0m")
            continue
    print(f"\nAciertos: {c}/10 - {c*100//10}%")

if __name__ == '__main__':
    try:
        main()
    except:
        print()
        exit()
