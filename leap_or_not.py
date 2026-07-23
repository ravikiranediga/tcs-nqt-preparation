# Check Whether a Year is a Leap Year or Not in Python
num=int(input("Enter a Year:"))
if num%4==0 and num%100!=0 or num%400==0:
    print(num,"is a Leap Year")
else:
    print(num,"is not a Leap Year")




# Using Calender Module 
import calendar

def is_leap_year(year):
    return calendar.isleap(year)

# Test with year 2000
year = 2000
print(f"{year} is a leap year: {is_leap_year(year)}")


#  Using Lamda Function
# Lambda function to check leap year
is_leap_year = lambda year: True if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else False

# Test with year 2000
year = 2028
print(f"{year} is a leap year: {is_leap_year(year)}")
