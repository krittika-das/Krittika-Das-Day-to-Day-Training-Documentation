def is_leap(yr):
    return (yr%4==0 and yr%100!=0) or (yr%400==0)

print(is_leap(2024))