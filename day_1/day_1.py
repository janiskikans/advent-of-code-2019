import math

# Caluclate the required fuel for a module
def calculate_required_fuel_for_module(mass):
    return math.floor(mass / 3) - 2

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
        total_required_fuel += calculate_required_fuel_for_module(int(module_mass))
        
    return total_required_fuel
    

if __name__ == '__main__':
    print(get_total_required_fuel())