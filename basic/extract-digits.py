# Extracting digits from a given number / Counting number of digits

def extract_digits(num):
    count = 0
    while(num > 0):
        last_digit = num % 10
        print(last_digit)
        count = count + 1
        num = num // 10
    return count

num = 12345
print("Number of digits ", extract_digits(num))

"""
Time Complexity will O(log10(N))
as it is equivalent to number of times the number is divisible by 10
"""