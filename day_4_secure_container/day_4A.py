"""
Day 4: Secure Container. Part A

Known facts about the password:
    1) 6 digit number
    2) The value is in the given range
    3) Two adjacent digits are the same (like 22 in 122345)
    4) Going from left to right, the digits never decrease -
        they increase or stay the same (like 111123 or 135679)
        
Goal - find all possible password combinations that match the given information.

"""

import re
    
def has_same_two_adjecent_digits(combination):
    if (re.search(r"(\d)\1", str(combination))):
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
        if has_same_two_adjecent_digits(combination) and has_all_increasing_digits(str(combination)):
            matching_combinations.append(combination)
            print("Matching password: " + str(combination))
            
    return len(matching_combinations)

if __name__ == '__main__':
    range_min = 168630
    range_max = 718098
    
    matching_password_count = str(find_all_validate_passwords(range_min, range_max))
    print("Matching password count: " + matching_password_count)