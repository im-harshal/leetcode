# Check if given number is an armstrong's number
# 371 is one such number because 3^3 + 7^3 + 1^3 = 371
# Leetcode : 1134

# Extract the digits, get the sum and compare to the original

# Way 1 - will only work for 3 digit numbers
def arm_num(num):
    dup = num
    sum_num = 0
    while num > 0:
        last_digit = num % 10
        num = num // 10
        sum_num = sum_num + last_digit ** 3
    return sum_num == dup
    
# Way 2 - will work for n digit number
def arm_num2(num):
    dup = num
    leng = len(str(num))
    sum_num = 0
    while num > 0:
        last_digit = num % 10
        num = num // 10
        sum_num = sum_num + last_digit ** leng
    return sum_num == dup

num = 1634
print("Way 1 - Num ", num, " is an Armstrong's number :", arm_num(num))
print("Way 2 - Num ", num, " is an Armstrong's number :", arm_num2(num))