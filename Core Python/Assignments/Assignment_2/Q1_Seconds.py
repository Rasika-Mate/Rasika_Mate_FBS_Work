# 1. Convert the time entered in hh,min and sec into seconds.

hrs = int(input("Enter Hours: "))
min = int(input("Enter Minutes: "))
sec = int(input("Enter Seconds: "))

total_sec = hrs * 3600 + min * 60 + sec
print("Total seconds:", total_sec)
