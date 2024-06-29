# Works on the extract logic 
# Does not considers negative number and range of integer

def reverse_num(num):
    rev_num = 0
    while num > 0:
        last_digit = num % 10
        num = num // 10
        rev_num = (rev_num * 10) + last_digit
    return rev_num

num = 40100
print("Reverse of ", num, " is", reverse_num(num))