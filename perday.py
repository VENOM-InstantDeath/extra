from datetime import datetime

def main():
    n = datetime.now()
    h, m = (n.hour, n.minute)
    s = (h*3600)+(m*60)
    r = s*100//86400
    print(f"Ha transcurrido un {r}% del día")

if __name__ == '__main__':
    main()
