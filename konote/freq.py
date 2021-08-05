from datetime import datetime, timedelta, date

def today():
    today = date.today()
    return today

def tmrw(today):
    tmrw = today + timedelta(days=1)
    print(tmrw)

def main():
    tmrw(today())

if __name__ == "__main__":
    main()
