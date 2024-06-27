from datetime import datetime, timedelta
from collections import Counter

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def calculate_popular_sum(start_date, end_date):
    current_date = start_date
    sums_counter = Counter()
    
    while current_date <= end_date:
        day = current_date.day
        month = current_date.month
        year = current_date.year
        
        sum_value = day + month + sum_of_digits(year)
        sums_counter[sum_value] += 1
        
        current_date += timedelta(days=1)
    
    most_common_sum = sums_counter.most_common()
    return most_common_sum

start_date = datetime(1000, 1, 1)
end_date = datetime.today()

most_common_sum, count = calculate_popular_sum(start_date, end_date)

print("The most popular sum is {most_common_sum} which appears {count} times.")

