import sys
import datetime

if __name__ == '__main__':
    print datetime.date(datetime.date.today().year, datetime.date.today().month - 1, 1).strftime("%Y-%m") + "_data.xls"
