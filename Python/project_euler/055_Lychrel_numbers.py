
def reverse(x):
    return int("".join(list(str(x))[::-1]))

def is_palindrome(x):
    str_x = str(x)
    len_div_2 = (len(str_x))//2 + len(str_x)%2
    first_half = str_x[:len_div_2]
    second_half = str_x[len_div_2-((len(str_x))%2):]
    for i in range(len_div_2):
        if first_half[i] != second_half[-(i+1)]:
            return False
    
    return True

result = 0
for i in range(1,10001):
    current = i
    reverse_current = reverse(current)
    count = 0
    while count < 50:
        current_sum = current + reverse_current        
        if is_palindrome(current_sum): 
            count = 70
            break

        current = current_sum
        reverse_current = reverse(current)
        count += 1
    if count != 70:
        result += 1

print(result)
    
