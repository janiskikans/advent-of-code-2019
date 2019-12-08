"""
Day 4: Secure Container. Part B

Known facts about the password:
    1) 6 digit number
    2) The value is in the given range
    3) Two adjacent digits are the same (like 22 in 122345)
    4) Going from left to right, the digits never decrease -
        they increase or stay the same (like 111123 or 135679)
    +
    5) The two adjacent matching digits are not part of a larger group of matching digits!
        
Goal - find all possible password combinations that match the given information.

"""

import re
    
def has_same_two_adjecent_digits(combination):
    adjecent_digit_occurances = 0
    combination_length = len(combination)
    
    for digit in range(1, combination_length):
        if (combination[digit] == combination[digit-1]):
            adjecent_digit_occurances += 1
        elif (adjecent_digit_occurances == 1):
            break
        else:
            adjecent_digit_occurances = 0
    
    if (adjecent_digit_occurances == 1):
        return True
    return False

def has_all_increasing_digits(combination):
    number_list = [int(x) for x in combination] 
    
    if sorted(number_list) == number_list:
        return True
    
    return False

def find_all_validate_passwords(range_min, range_max):
    matching_combinations = []
    
    for combination in range(range_min, range_max):
        if has_same_two_adjecent_digits(str(combination)) and has_all_increasing_digits(str(combination)):
            matching_combinations.append(combination)
            print("Matching password: " + str(combination))
            
    return len(matching_combinations)

if __name__ == '__main__':
    range_min = 168630
    range_max = 718098
    
    matching_password_count = str(find_all_validate_passwords(range_min, range_max))
    print("Matching password count: " + matching_password_count)