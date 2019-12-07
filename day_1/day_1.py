import math

# Calculate the required fuel for a module
def calculate_required_fuel_for_module(mass):
    return math.floor(mass / 3) - 2

# Caluclate the total required fuel for module (including extra additional fuel for fuel)
def calculate_required_fuel_plus_additional_fuel(mass):
    total_required_fuel = 0
    required_fuel = calculate_required_fuel_for_module(mass)
    
    while (1):
        total_required_fuel += required_fuel
        required_fuel = calculate_required_fuel_for_module(required_fuel)
        
        if (required_fuel <= 0):
            break
        
    return(total_required_fuel)

# Read the input file of module masses to a list
def read_modules_to_array(input_file):
    with open(input_file) as f:
        content = f.readlines()
    return content

# Return total required fuel
def get_total_required_fuel():
    input_file = 'input.txt'
    module_masses = read_modules_to_array(input_file)
    
    total_required_fuel = 0
    for module_mass in module_masses:
        total_required_fuel += calculate_required_fuel_plus_additional_fuel(int(module_mass))
        
    return total_required_fuel
    

if __name__ == '__main__':
    print(get_total_required_fuel())