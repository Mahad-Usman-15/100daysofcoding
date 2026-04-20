import math
# Given a year, return the century it is in.
# 1900 --> 19
# 1601 --> 17
# 2001 --> 20
# 2742 --> 28
def get_century(yr):
  return (yr-1)//100 + 1
print(get_century(1900))
print(get_century(1601))




