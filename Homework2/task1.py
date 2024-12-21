year=(int(input("Enter year: ")))

def days(a):
    return year*a
day = days(365)
print(f"In {year} years has {day} days ")

def weeks(b):
    return year*b
week = weeks(52)
print(f"In {year} years has {week} weeks ")

def month(c):
    return year*c
month = month(12)
print(f"In {year} years has {month} month ")

def hour(d):
    return year*d
hour = hour(8760)
print(f"In {year} years has {hour} hours ")