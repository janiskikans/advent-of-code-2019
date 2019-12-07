# Read opcodes from input file to list of ints
def read_opcodes_to_list():
    opcode_list = []
    file = open('input.txt', 'r')    

    for line in file.readlines():
        opcode_list = line.rstrip().split(',')
        
    for i in range(0, len(opcode_list)): 
        opcode_list[i] = int(opcode_list[i]) 

    return opcode_list

# Add two numbers
def add(number_1, number_2):
    return number_1 + number_2

# Multiply to numbers
def multiply(number_1, number_2):
    return number_1 * number_2

# Get the resulting opcode list
def get_opcode_output():
    opcode_output_list = read_opcodes_to_list()
    
    opcode_output_list[1] = 12
    opcode_output_list[2] = 2
    
    current_opcode_position = 0
    while (current_opcode_position < len(opcode_output_list)):
        current_opcode_value = opcode_output_list[current_opcode_position]
        first_input_value = opcode_output_list[opcode_output_list[current_opcode_position + 1]]
        second_input_value = opcode_output_list[opcode_output_list[current_opcode_position + 2]]
        result_position = opcode_output_list[current_opcode_position + 3]
        
        if (current_opcode_value == 1):
            opcode_output_list[result_position] = add(first_input_value, second_input_value)
        
        if (current_opcode_value == 2):
            opcode_output_list[result_position] = multiply(first_input_value, second_input_value)
            
        if (opcode_output_list[current_opcode_position + 4] == 99):
            print('STOP!')
            break
        
        current_opcode_position += 4
    
    return opcode_output_list
        

if __name__ == '__main__':
    print(get_opcode_output())
    