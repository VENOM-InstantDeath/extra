import random

def choice(s):
    s = [i.strip() for i in s.split(',')]
    return random.choice(s)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print(choice(sys.argv[1]))
        exit(0)
    s = input('list: ')
    print(choice(s))
