# SecondsToTime
## SecondsToTime is a simple function that converts time in seconds to seconds, minutes, hours and days
Not much because I'm unable to make a Python package for of this lol

Example of function in use:
```py
time = SecondsToTime(72)

print(f"{time[0]} days")
print(f"{time[1]} hours")
print(f"{time[2]} minutes")
print(f"{time[3]} seconds")
```
```py
0 days
0 hours
1 minutes
12 seconds
```
---
```py
time1 = SecondsToTime(45)
time2 = SecondsToTime(415)
time3 = SecondsToTime(9583)
time4 = SecondsToTime(105725)

print(time1)
print(time2)
print(time3)
print(time4)
```
```py
[0, 0, 0, 45]
[0, 0, 6, 55]
[0, 2, 39, 43]
[1, 5, 22, 5]
```

### Feel free to suggest changes
