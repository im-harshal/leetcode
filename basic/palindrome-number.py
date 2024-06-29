# Given a number, reverse it and compare to check if it is the same
# Leetcode : 9

# Way 1
def pal_check(num):
    dup = num
    reverse_num = 0 
    while num > 0:
        last_digit = num % 10
        num = num // 10
        reverse_num  = reverse_num * 10 + last_digit
    
    if(reverse_num == dup):
        return True
    else:
        return False
    
# Way 2
def pal_check2(num):
    num = str(num)
    if num == num[::-1]:
        return True
    else:
        return False

num = 12321
print("Way 1 ", num, " is palindrome :", pal_check(num))
print("Way 2 ", num, " is palindrome :", pal_check2(num))