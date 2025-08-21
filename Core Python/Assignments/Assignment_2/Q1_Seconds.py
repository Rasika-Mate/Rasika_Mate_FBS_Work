# 1. Convert the time entered in hh,min and sec into seconds.

hrs = int(input("Enter Hours: "))
min = int(input("Enter Minutes: "))
sec = int(input("Enter Seconds: "))

hrs_sec = hrs*3600
min_sec = min*60
total_sec = hrs_sec+min_sec+sec

print("Seconds is",total_sec)