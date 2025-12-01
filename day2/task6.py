# Determine if a year is a leap year.
# for leap year
# notdived by 100
# divided by 400 and 4
def is_leap_year(year:int):
    if year%4==0:
        print(f'{year} is leap year')
    else:
        print(f'{year} is not a leap year')

# Method2
# Determine if a year is a leap year.

def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


year = 2030
print(f"{year} is {'a' if is_leap_year(year) else 'not a'} leap year")
