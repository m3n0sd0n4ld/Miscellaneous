#!/usr/bin/python3

year = "XXXX"
month = "XX"

for i in range(2,9):
    day = "0"+str(i)
    print("{}{}{}".format(year,month,day))
    print("{}{}{}".format(day,month,year))
    print("{}{}{}".format(month,day,year))
    print("{}-{}-{}".format(year,month,day))
    print("{}-{}-{}".format(day,month,year))
    print("{}-{}-{}".format(month,day,year))
    print("{}/{}/{}".format(year,month,day))
    print("{}/{}/{}".format(day,month,year))
    print("{}/{}/{}".format(month,day,year))